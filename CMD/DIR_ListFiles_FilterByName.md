# List files, filter by name

    This will list the files that contain a string in the file name
    
## Code:

    dir <path>\*<string filename contains>* /s /b /a-d                          # Searches for file names only recursively
    dir <path>\*<string foldername contains>* /s /b /o:n /ad                      # Searches for folder names only recursively