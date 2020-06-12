# Disk Partition

    This will allow to partition disks without sd formatter or the like, mostly for raspberry pi'sd
    
## Steps

    Open CMD as admin
    
    diskpart                        # opens Disk Partitioner (If cmd hangs, remove sd)
            
    list disk                       # find your partition you want to formatter
            
    select disk <Disk>              # pick that disk
            
    clean                           # cleans the disk of all contents
            
    list disk                       # verify the disk is still selected by *
        
    create partition primary        # creates partition
        
    select partition 1              # select created partition
        
    active                        # make sure partition is active
    
    format FS=NTFS label=Data quick # formats the drive
    
    assign letter=d                 # assing partition a letter
    
    exit