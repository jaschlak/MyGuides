# Find File Size Recursive

    Navigate to the place you want the file saved, modify the command to look in the folder you want it to, run the command and find all the values in your test.txt
    Note you may need permission to write to the folder you save to
    
## Command:

    @echo off & for /R "<insert folder path>" %A in (*.*) do echo %~fA %~zA >> test.txt
    
## Keep in mind echo is now off, turn it back on with

    @echo ON