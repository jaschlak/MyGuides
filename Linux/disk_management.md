# Disk Management

    Hard Disk Management, partitions/lvms etc
    
## lookup info on partitions

    df -h                                       #size, %'s, mounted location
    fdisk -l                                    #sectors and allocation and types (disks with table of partitions,if any on each disk)
    fdisk <path> *return* p                     #sectors and allocation of mounted disk
    fdisk <path> *return* F                     #show free, unpartioned space
    parted *return* print free                  #show free space on machine
    
    # lblk & blkid can be used to find UUID
    
    
    
## mount device(temperary until boot)

    mount                                       # see what is currently mounted (physical and virtual)
    df -h                                       # see what is physically mounted
    mount <src filesystem path> <dest path>     # ex: mount /dev/sda/ /opt 
    umount <path>                               # unmount, ex: umount /opt, umount /dev/sdb3
    
## mount permanent: fstab

    example fstab file: (used tab here but single space is what should be used)
    #   device  mount point   FS    options  dump    fsck
    /dev/sda2   /             xfs   defaults    0       1
    /dev/sda1   swap          swap  defaults    0       0
    
    # examples w proper spaceing:
    UUID=dbae4fe7-b06f-4319-85dc-b93a4a16b17 / xfs defaults 0 1
    LABEL=opt /opt ext4 defaults 1 1
    /dev/sda1 swap swap defaults 0 0
    
    device: <path to device>, <label to device>, <uuid of device>
    mount point: <path to be mounted>
    FS: <file system type> (same as type in mkfs command)
    options: <options for file system (typically defaults, consult manual for file system if need)
                                      (multiple allowed, uses comma with no space for multiple options)
    dump: <0 or 1> (perform backup, rarely used)
    fsck: <0, 1, or 2>  (check file system? 0=nocheck, 1=check first, 2=check next)
    
## labelling

    # add labeling to device
    e2label <partition path> <label name>
    
    
    
## file systems

    ls -l .sbin/mkfs*                           # see file system types
    man <path from above command>               # see more info on file system types ex: man /sbin/mkfs.xfs
    mkfs -t <type> <device>                     # types: ext3, ext4. device = path
    
## swap space

    workflow:
    1) prepare space
        mkswap <partition path>
    2) enable
        swapon <path to device>
        
    swapon -s                                   # see swaps currently in use
    
---------------------------------------------------------------------------------------------
# LVM Logical Volume Manager

    LVMs can aggregate multiple storage devices into a single logical volume
    Can expand or shrink filesystems while system is online and fully accessible
    Can use LVM to do data mirroring
    Can make point int time snapshots
    
## Storage Hierarchy

    File Systems
    Logical Volumes (LV)    ^                   # lvs or lvdisplay or lvdisplay -m
    Volume Groups (VG)      ^                   # vgs
    Physical Volumes (PV)   ^                   # pvs
    Storage Devices         ^                   # lvmdiskscan    
    
## searching

    parted                                      # see free space on machine    
        print free                              
    parted <physical disk path>
        print free
    lvmdiskscan                                 # see storage devices available
    pvdisplay -m                                # see physical device <--> logical device mapping
    lsblk                                       # see device mapping and mounting points
    lsblk -p                                    # see full paths to devices in mapping
    lsblk -f                                    # see file system type
    lsblk -m                                    # see permissions info
    lsblk -o NAME,KNAME,MOUNTPOINT              # example of printing explicit columns
    pvs                                         # see physical volumes
    vgs                                         # see volume groups
    lvs                                         # see logical volumes
    lvdisplay                                   # see more logical volumen info (including path)
    lvdisplay -m                                # shows physical volume mapped
    
    df -h                                       # see human readable info on filesystem 
    fdisk -l                                    # see actual paths to drives (storage attached to linux system)
    
## create

    vgcreate <vg_name> <pv_path(s)>             # create volume group from physical volume(s)
    lvcreate -L <Size> -n <lv_name> <vg_source_name> # ex: lvcreate -L 20G lv_data vg_app
    mke2fs -t <type> <path to lv>               # make filesystem on lvm
        mkdir <dir to mount>                    # still needed to make a directory
        mount <path to lv> <mount path>         # now can be seen in filesystem
    
## Extend LVM

    1) add space to VM
    2) scan for disk
        lvmdiskscan
    3) create phsyical volume
        pvcreate <path from step 2>
    4) extend volume group
        vgextend <vg_name> <path from step 2>
    5) check space is free in physical volume/volume group
        pvs
        vgs
    6) extend free space to logical volume from volume group
        lvextend -L +<amount> -r <logical volume path>
        
        example:
        lvextend -L +5G -r /dev/vg_app/lv_data
        lvextend -L +100%FREE -r /dev/vg_app/lv_data                # -r resize
        lvextend -L +100%FREE /dev/vg_app/lv_data
        
    7) make sure changes made, confirm file system and lvm are the same size
    
        df -h <mount point>
        lvs
        
    8) if no resize in step 6, resize filesystem:
        resize2fs <path to logical volume>
        
## Deleting volumes

    umount <filesystem path>
    lvremove <path to logical volume>
    vgreduce <volume group name> <physical volume path>
    pvremove <physical volume path to remove>
    vgremove <volume group name>                            # can remove since not connected to physical volume
    
    
## Disk Cleanup (logrotates)

    --perform daily log rotation now
    sudo logrotate -d /etc/logrotate.d

    --find largest files/directories
    sudo du -a / 2>/dev/null | sort -n -r | head -n 20

    --clean journalctl down to 100MB
    sudo journalctl --vacuum-size=100M

    --Restart journald 
    sudo systemctl restart systemd-journald.service
