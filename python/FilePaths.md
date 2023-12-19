# Adding/Deleting File Paths

## Modules needed for import

    import os, sys
    
## Commonly used commands

    path = \<Filepath using '/'\>                               # create file path
    sys.path.insert(0, path)                                    # insert file path to the system
    print(sys.path)                                             # see current file paths
    sys.path.insert(0, path)                                    # remove file path
    os.listdir('<path>')                                        # get list of files in directory
    
    
    os.chdir('<file path>')                                     # Add a working directory
    os.path.abspath(__file__);                                  # Move Spyder path to this files directory    

