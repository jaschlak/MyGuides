# Expanding disk

    Expanding disk in a VM environment. In this environment there is a prexisiting sda1 and sda2
    
## Steps

    *** expand the hard disk space for the VM first ***

    lsblk                           # detect disks and how much space is used
    
    sudo fdisk                      # open disk formatter
    p                               # show all information about pre-existing partitions
    
    d                               # initiate a partition delete
    2                               # delete part #2
    
    d                               # initiate a partition delete
    1                               # delete part #1
    
    d                               # create a new partition
    p                               # create it as primary partition
    enterx2                         # use default values for start and end sectors
    N                               # Do not remove old signature from the hard disk
    
    p                               # show all information about post change partitions
    
    w                               # write all changes made since fdisk was opened (may have to reboot)
    
    
    Note: this will expand the partition on the hard disk but the file system has not been allowed to use the space yet
    
## Expand file system to the size of the expanded hard disk

    lsblk                           # detect disks and how much space is used
    
    df -h /                         # shows file system space used and how much disk space is available
        
    sudo resize2fs /dev/sda1        # expand file system
    
    sudo reboot                     # reboot and check sizes again
    
    