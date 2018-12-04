# Find current time and date

    This is a formatable way to find time and date
    
## Note:

    This is a modification of the commands %time% %date%
    echo %time% prints in the format of Tue 12/04/2018
    echo %date% prints in the format of 17:39:15.94
    
    This code parses the day of the week in date and milliseconds in time
    
    
    More information at:
    
    
## Code:

    for /F "tokens=2" %i in ('date /t') do echo %i %time:~,-3%
    