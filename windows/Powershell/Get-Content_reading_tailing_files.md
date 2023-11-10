# Get-Content

    This was originally documented for tailing logs but more general instructions for reading files are now included
    
## Command

    Get-Content -Path <path>
    Get-Content <insert log> -Tail 2 –Wait
    Get-Content -Path <path> -First 2
    Get-Content -Path <path>\* -Include '*.txt'
    
    
    Get-Content -Path <path> -Tail 5 | Where-Object {$_ -like '*Fail*'}
    
## Examples

    # example 1: loop through serverlist and get information on each server (clearly serverlist.txt needs to exist with list of servers you have network access to)
    
        $servers=Get-Content 'serverlist.txt'
        foreach($server in $servers)
        {
            Get-WmiObject -Class Win32_Operatingsystem -ComputerName $server | Select-Object @{'Name'='ServerName';'Expression'={$_.PSComputerName}}, @{'Name'='Last Restart Time';'Expression'={$_.ConvertToDateTime($_.LastBootUpTime)}}
        }
        
    # example 2: loop through serverlist.txt, get last reboot time, output to new file
    
        Clear-Content exampleoutputfile.txt

        $serversInFile = 'serverlist.txt'
        $outputFile = 'exampleoutputfile.txt'

        "Report: Last Reboot Time of All Servers:" | Out-File exampleoutputfile.txt

        $servers=Get-Content $serversInFile

        foreach($server in $servers)
        {
            $serveroutput = Get-WmiObject -Class Win32_Operatingsystem -ComputerName $server | Select-Object @{'Name'='ServerName';'Expression'={$_.PSComputerName}}, @{'Name'='Last Restart Time';'Expression'={$_.ConvertToDateTime($_.LastBootUpTime)}}
            
            $serveroutput.ServerName + ", Last Reboot: " + $serveroutput.'Last Restart Time' | Out-File $outputFile -Append
        }
        
    # example 3: loop through serverlist.csv, output connectiontest info to outputexample.csv
    
        $inputcsv = 'serverlist.csv'
        $outputcsv = 'outputexample.csv'

        Clear-content $outputcsv
        $servers = Import-CSV $inputcsv

        foreach ($server in $servers)
        {
            Test-Connection -ComputerName $server.ServerName -Count 1 | Out-File $outputcsv -Append
        }
        
    # example 4: loop through serverlist.xml, output data for servers to terminal
    

        '''
        <?xml version="1.0"?>
        <ServerList>
          <Server>
              <Name>CENTRALSERVER</Name>
              <IP>192.168.225.10</IP>
              <Location>Asia</Location>
          </Server>
            <Server>
              <Name>VM1</Name>
              <IP>192.168.225.11</IP>
              <Location>USA</Location>
          </Server>
            <Server>
              <Name>VM2</Name>
              <IP>192.168.225.12</IP>
              <Location>INDIA</Location>
          </Server>
        </ServerList>
        '''



        [xml] $servers = Get-Content serverlist.xml

        #$servers.ServerList.Server.Location

        foreach ($server in $servers.ServerList.Server)
        {
            'The server: ' + $server.Name + ' with ip: ' + $server.ip + ' is located in: ' + $server.Location
        }