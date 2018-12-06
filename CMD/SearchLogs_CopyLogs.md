# Search through files for string, copy files to new folder

    The purpose of this is to find a way to pull all logs at the current time
    This is designed to be triggered by an automation rule
    
## Code:

    :: change directory to file path
    CD %~dp0
    :: make directories that will be used
    MKDIR <search path>
    MKDIR <destination path>
    MKDIR <extended destination path> :: This path would simulate the directories the files you are pulling have, you could maybe truncate or use tokens in a for loop

    :: Creates string for last 2 hours
    SET this_hour=%time:~0,2%
    IF %this_hour% EQU 00 (set /a last_hour=11) ELSE (set /a last_hour=%this_hour%-1)
    IF %last_hour% EQU 00 (set /a last2hour=11) ELSE (set /a hour_sub2=%last_hour%-1)

    :: Clears old file containing filenames to be coppied
    <nul (set/p z=) > .\logfiles\filelist.txt

    :: Searches all logs for any entries in the last 2 hours, writes file names to a file
    FINDSTR /m /C:"%date:~-4%-%date:~4,2%-%date:~7,2% %this_hour%%time:~2,1%" <search path>\*<file string>* >> <destination path>\filelist.txt
    FINDSTR /m /C:"%date:~-4%-%date:~4,2%-%date:~7,2% %last_hour%%time:~2,1%" <search path>\*<file string>* >> <destination path>\filelist.txt
    FINDSTR /m /C:"%date:~-4%-%date:~4,2%-%date:~7,2% %hour_sub2%%time:~2,1%" <search path>\*<file string>* >> <destination path>\filelist.txt
    :: Add as many items to the list as you like, this example searches for items with events noted in the last 3 hours

    :: Copies all listed files to new directory <extended destination path>\filename (%%A is the name of the file with the path it was found in)
    FOR /F "tokens=*" %%A IN (<destination path>\filelist.txt) DO COPY %%A .\logfiles\%%A

    :: Pausing to view process when manually run
    PAUSE