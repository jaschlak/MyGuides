# Disk Management

    Currently for getting storage information. For disk formatting instructions see "diskpart.md"
    
## See all letter drive information

    wmic LOGICALDISK LIST BRIEF

## DiskPart

    diskpart
    LIST DISK
    (look for disk that looks right)
    SELECT DISK
    DETAIL DISK                                                 (Make sure "Ltr" here matches the letter in wmic command above
    