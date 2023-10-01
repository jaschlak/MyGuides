#Batch Commands

    This is meant to be simple examples of things you can add to your batch scripts
    
## Simple Commands

    ECHO ON                 # default prints echo text and command output
    ECHO OFF                # turn off command output, keep test
    @ECHO OFF               # turn off command print as well as command output
    VER                     # get Windows Version
    CD                      # print Current Directory
    CD <path>               # change Directory to path
    CD ..                   # change Directory to parent directory
    CHOICE                  # give user choice input, /?, /C list choices, /M give message
    DIR                     # list directories in current path
    DIR <path>              # directories in explicit path /?, /A all files, /AH only hidden files
    DATE                    # change date
    ECHO %DATE%             # print date
    TIME                    # change time
    ECHO %TIME%             # print time
    CLS                     # clear Screen
    TASKLIST                # print list of tasks, pid, session, memory used
    PAUSE                   # pause until user gives input to move ON
    REM                     # leave a remark (comment line out)
    TITLE                   # set title for cmd console
    SHUTDOWN                # shutdown computer /r restart
    COMP <path1> <path2>    # compare 2 file sizes
    SORT <path>             # sort lines in file
    HELP                    # prints available commands with description
    HELP <command>          # get documentation on specific command
    COPY <path1> <path2>    # copy file(s) from source to destination path
    XCOPY <path1> <path2>   # copy files, directories, and subdirectories from source to destination
    DEL <path>              # delete file, /P prompt user for verification
    MOVE <path1> <path2>    # move file/folder from source to dst
    ATTRIB                  # gives attributes of all files (has changed since last backup?)
    ATTRIB +r <path>        # make file read only 
    ATTRIB +h <path>        # make file hidden
    ATTRIB -h <path>        # make file shown
    FIND <path> <string>    # search for string in path
    TYPE <path>             # print the contents of file in path
    