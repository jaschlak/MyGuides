# Get Services

    Get Services on machine using powershell along with it's state and description
    
## Usage

    Get-Service
    Get-Service | Get-Member                                                                    # get attributes available to select
    Get-Service | Select-Object Name, DisplayName, StartType, Status                            # select specific attributes (comma separated)
    Get-Service | Select-Object Name,Status | Where-Object {$_.Name -eq 'BITS'}                 # select attributes for service "BITS"
    Get-Service | Select-Object Name,Status | Where-Object {$_.Name -eq 'BITS'} | Stop-Service  # also stop the BITS service