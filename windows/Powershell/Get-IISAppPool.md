# Get-IISAppPool

    How to get information about the App Pools in IISAppPool
    
## Commands

    Get-IISAppPool                                      # See default information for all app Pools
    Get-IISAppPool | Get-Member                         # See all properties/methods for Get-IISAppPool
    Get-IISAppPool | Select-Object Name                 # See Name only for all app pools
    Get-IISAppPool | Select-Object -ExpandProperty Name # See values only
    
## More specific examples

    # Get all app pools in which the application points to a certain directory
    Get-WebApplication | Select-Object applicationPool,PhysicalPath | Sort-Object -Property applicationPool -Unique | Where-Object {$_.PhysicalPath -like "*<directory_filter_str>*"} | Select-Object applicationPool