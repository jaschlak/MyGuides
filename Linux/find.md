# Find

    Searching desktop for files/directories
    
## find params (searches file name)

    find <path> -name <pattern>
    find <path> iname <pattern>                         # ignores case
    find <path>-ls                                      # does ls on returned paths
    find -mtime <time delta>                            # finds files within modification age specified
    find <path> size <num>                              # finds files within size
    find <path> -newer <file>                           # finds files newer than specified file
    find <path> -exec command {} \;                     # runs command against the file
    
## locate(searches by index, might be delay when creating a file and locating it)

    locate <pattern>

    