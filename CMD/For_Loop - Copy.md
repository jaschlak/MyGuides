# For Lister Loop

    This loop lists things and takes an acction with that lists
    
## Structure

    for /f
    tokens=<#>          # tokens to save after split (sections of strings)
    delims=<#>          # delimeter to split string up by
    %%<char>            # index saved
    do(<command>)       # executes defined command
    
## Example (string)

    @echo off
    for /f "tokens=1 delims =0" %%a in ('echo dog yo bob') do(echo %%a)
    
## Example (file)
    
    @echo off
    FOR /F "tokens=*" %%A IN (<path>\filelist.txt) DO COPY %%A ..\Entre\logfiles\%%A

## Example run file 20 times

    for /L %i in (1,1,20) do @<process name>
    for /L %i in (1,1,20) do @notepad.exe