#grep

    Useful grep and awk commands
    
## Grep

    grep --regexp="<search string>" --count <path to file>                          # use regex to search for string in a file and get count
    
## Awk 

    source:https://www.geeksforgeeks.org/awk-command-unixlinux-examples/ (command instead of filename is supported)

    awk '<search criteria>' {print} <filename>                                      # search for string in file (command instead of filename is supported)
    awk -F':' '{print $1}' <filename>                                               change delimeter to ":"
    awk '{print $1,$4}' <filename>                                                  # print the 1st and 4th column of each row, splits columns with default ' ' char
    awk '{print NR,$1,$4}' <filename>                                               # add line number to search above
    awk '{print $1,$NF} <filename>                                                  # adds last column in row
    awk 'NR==3, NR==6 {print NR,$0}' <filename>                                     # display columns 3-6
    awk '{print NR "-" $1}' <filename>                                              # add a character to the output
    awk 'NF > 0' <filename>                                                         # print any non-empty line (more than 0 columns)
    awk 'length($0) > <char length>' <filename>                                     # print lines with more than char length
    awk '{ if (length($0) > max) max = length($0) } END { print max }' <filename>   # get length of longest line
    awk 'END { print NR }' <filename>                                               # get a line count
    awk '{ if($<column number> == "<input text>") print $0;}' <filename>            # seach column number for input text
    awk 'BEGIN { for(i=1;i<=6;i++) print "square of", i, "is",i*i; }'               # print the square of numbers from 1 to 6
    awk -F':' '{print $3 "*" $4 "=" $3*$4}' <filename>                              # change delimeter to ":" and multiply lines 3 and 4
    