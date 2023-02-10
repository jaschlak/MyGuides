# Power CLI

    Nots and examples on using powercli
    
## Windows Online Install

    Install-Module -Name VMware.PowerCLI 
    
## Windows Offline Install (https://vdc-download.vmware.com/vmwb-repository/dcr-public/847b8d79-9752-43d3-8217-8270ab647679/1e992a3d-ac47-4453-8182-457145215c40/GUID-3034A439-E9D7-4743-ABC0-EE38610E15F8.html)

    1) Download ZIP
        https://developer.vmware.com/web/tool/vmware-powercli
        Move Zip to isolated folder
        
    2) Find location you can extract to for PowerShell Modules
        $env:PSModulePath
        
    3) Extract Zip
    
    4) Move extracted folders to folder path from Step 2
    
    5) Unblock folder path
        Get-ChildItem -Path '<folder path selected in step 2>' -Recurse | Unblock-File

## Using

    -- List Available PowerCLI Modules (confirm installation)
    Get-Module VMware* -ListAvailable
    
    -- ignore cert on login
    Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
    
    -- connect to vcenter
    Connect-VIServer -Server <vcenter destination>
    
    -- Get List of VMs
    Get-VM
    
    -- Get Attributes
    
        -- specific stat
        Get-Stat -Entity (Get-vm "<VM_name>") -Stat "cpu-usage.average"
        
        -- daterange
        Get-Stat -Entity (Get-vm "<VM_name>") -Start ((get-date).AddDays(-1))
        
        -- multiple attributes
        Get-Stat -Entity (Get-vm "<VM_name>") -Stat @("cpu.usage.average","cpu.usagemhz.average")
    
        -- realtime
        Get-Stat -Entity (Get-vm "<VM_name>") -Realtime
    
    
    -- print VM info
    $View = Get-Vm "<VM_name>" | Get-View
    [PSCustomObject]@{
    Name          = $View.Name
    HostName      = $View.Guest.Hostname
    GuestState    = $View.Guest.GuestState
    GuestFullName = $View.Guest.GuestFullName
    IPAddress     = $View.Guest.IPAddress
    ToolsStatus   = $View.Guest.ToolsStatus
    ToolsVersion  = $View.Guest.ToolsVersion
    Network       = $View.Guest.Net.Network
    NetworkIP     = $View.Guest.Net.IPAddress
    }
    
    -- use powershell script (with param) print_basic.ps1
    Param (
        [string]$VM
    )

    $View = Get-Vm $VM | Get-View
    [PSCustomObject]@{
        Name          = $View.Name
        HostName      = $View.Guest.Hostname
        GuestState    = $View.Guest.GuestState
        GuestFullName = $View.Guest.GuestFullName
        IPAddress     = $View.Guest.IPAddress
        ToolsStatus   = $View.Guest.ToolsStatus
        ToolsVersion  = $View.Guest.ToolsVersion
        Network       = $View.Guest.Net.Network
        NetworkIP     = $View.Guest.Net.IPAddress
    }
    
    -- Monthly report of all vms
    Get-VM | Where {$_.PowerState -eq "PoweredOn"} |Select Name, Host, NumCpu, MemoryMB, `
    @{N="CPU Usage (Average), Mhz" ; E={[Math]::Round((($_ | Get-Stat -Stat cpu.usagemhz.average -Start (Get-Date).AddDays(-30) -IntervalMins 5 | Measure-Object Value -Average).Average),2)}}, `
    @{N="Memory Usage (Average), %" ; E={[Math]::Round((($_ | Get-Stat -Stat mem.usage.average -Start (Get-Date).AddDays(-30) -IntervalMins 5 | Measure-Object Value -Average).Average),2)}} , `
    @{N="Network Usage (Average), KBps" ; E={[Math]::Round((($_ | Get-Stat -Stat net.usage.average -Start (Get-Date).AddDays(-30) -IntervalMins 5 | Measure-Object Value -Average).Average),2)}} , `
    @{N="Disk Usage (Average), KBps" ; E={[Math]::Round((($_ | Get-Stat -Stat disk.usage.average -Start (Get-Date).AddDays(-30) -IntervalMins 5 | Measure-Object Value -Average).Average),2)}} |`
    Export-Csv -Path C:\ps_script\vms_report.csv
    
        -- modify to specific vm, swap $_.PowerState -eq "PoweredOn" with: -Name <VM_name>
    
    -- more (https://pchawda.wordpress.com/2021/05/28/powercli-script-to-capture-cpu-memory-usage-stats-of-vms-from-vcenter/)

