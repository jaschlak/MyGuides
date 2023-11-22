# Powershell Get-PSDrive

    Get information about the drives (including Registry and more)
    Adding Get-WmiObject -Class win32_Logicaldisk here as well since it is relevant
    
# Scripts

    # get drives on machine
    Get-PSDrive
    Get-PSDrive -PSProvider FileSystem                                                                              # filter to only filesystems
    Invoke-Command -ComputerName <hostname> -ScriptBlock {Get-PSDrive -PSProvider FileSystem}                       # get filesystem drive info for remote machine
                    
    # get space information for drives on machine               
    Get-WmiObject -Class win32_Logicaldisk                                                                          # bytes only
    Get-WmiObject -Class win32_Logicaldisk | Select-Object DeviceID,FreeSpace,Size                                  # filter columns
    Get-WmiObject -Class win32_Logicaldisk | Select-Object @{'Name'='DriveName';'Expression'={$_.DeviceID}}, `      # round to gb
                                       @{'Name'='FreeSpace';'Expression'={[math]::Round($_.FreeSpace/1GB)}}, `
                                           @{'Name'='TotalSpace';'Expression'={[math]::Round($_.Size/1GB)}}
                                           
                                           
   # get space information for drives with rounding on remote machine
   Get-WmiObject -Class win32_Logicaldisk -ComputerName  <hostnames> | Select-Object PSComputerName, @{'Name'='DriveName';'Expression'={$_.DeviceID}}, `
                                                            @{'Name'='FreeSpace(%)';'Expression'={[math]::round(($_.FreeSpace/$_.Size)*100)}}, `
                                                            @{'Name'='FreeSpace';'Expression'={[math]::Round($_.FreeSpace/1GB)}}, `
                                                            @{'Name'='TotalSpace';'Expression'={[math]::Round($_.Size/1GB)}}