# File Location Tools

    General commands to help find specific files
    
## Show type of files

    file <filename>
    
    find . -name '*' -exec file {} \;                               # pipes list of files here into file commands
    
    file `ls`                                                       # method 2, note ` is a backtick, doesn't work if filename has spaces
    
    
## Show file sizes

    du
    
    du -h                           # display file sizes with units (human readable)
    
    du --threshold=<value><units>   # filter results files bigger than value
    
## Find certain types of files recursively

    find . -size <lowest possible filesize><unit>                       # unit c=bytes, m=megabytes...
    
    find -executable                                                    # only files that are executable
    
    find ! -executable                                                  # find files that are not eexecutable
    
## Search files for contents recursively

    grep -iRl "<text to find>" <path>                                   # -i ignore text case, -R recursive, -l show filenames instead of contents
    
## Return only unique lines from file

    sort <filename> | uniq -u
    
## Search file that has partial encrypted data

    cat <filename> | grep -a "<string to search for>"
    
## Find compression types with recursive compression

    file <filename>
    
    <decompression type> <filename> | file -
    
    <decompression type> <filename> | <next decompression type> | file -