# Powershell Read and Write Files

    I realized I only had readfiles so far and needed an obvious place for both read and write files. This structure will likely evolve.
    
## Read Files

    Get-Content -Path <filepath>
    Get-Content -Path <filepath> -Tail 5 -Wait
    Get-Content -Path <filepath> -First 5
    
## Write Files

    # write as txt or custom types
    Out-File -FilePath <filepath>
    Out-File -FilePath <filepath> -Append -Force
    
    # write as csv
    Export-CSV -Path <filepath>.csv
    <command> | Export-CSV -Path <filepath>.csv -Delimiter "`t"         # use tab delimeter
    <command> | Export-CSV -Path <filepath>.csv -NoClobber              # wont overwrite file
    <command> | Export-CSV -Path <filepath>.csv -NoTypeInformation      # don't include column/header types
    
    # html example 1: write as html (example, not one size fits all)
    
        # investigate columns (for column selection
        Get-Service | Get-Member
        
        # pick columns, convert to html, prepend/postpend , save html
            Get-Service | Select-Object Name,DisplayName,Status | ConvertTo-HTML -As Table -PreContent `
            "<h2>This report was generated $(Get-Date)</h2> </p>" -PostContent "</p>Thank You" `
            | Out-File <filepath>.html
        
        # run html file
        Invoke-Item <filepath>.html
        
    # html example 2: combine 2 command outputs into a single html file
    
        # define header
        $Header = @"
        <style>
        TABLE {border-width: 1px; border-style: solid; border-color: black; border-collapse: collapse;}
        TD {border-width: 1px; padding: 3px; border-style: solid; border-color: black;}
        </style>
        "@

        # collect data from OS and Services
        $os=Get-WmiObject -Class Win32_Operatingsystem -ComputerName localhost | ConvertTo-Html -As Table -PreContent "<h2>Report gerated on $(Get-Date) </h2>" | Out-String
        $services=Get-Service | select name, DisplayName, Status  | ConvertTo-Html -As Table  -PreContent "<h2>Hardware</h2>" | Out-String

        # convert output to html, define title, header, save html, run html
        ConvertTo-Html -Title "sys information for VM1 " -PreContent $os,$services -Body "<h2> Gathering OS Details <h2>" -Head $header | Out-File '<filepath>.html' 
        Invoke-Item <filepath>.html