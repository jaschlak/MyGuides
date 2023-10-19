# Get-ChildItem

	This will search for files in directories
	
## Use Cases

    Get-ChildItem -Path <path>
    Get-ChildItem -Path <path> | Select Name,LastWriteTime
    Get-ChildItem -Path <path> -Recurse -Include '*.txt'
    Get-ChildItem -Path HKLM:\HARDWARE                                  # use Get-Member for more attributes to select
    
## Recursive Example

	# structure
	Get-ChildItem -Path .\<known_folder>\*\<part_file>*.<ext> -recurse
	
	# example
	Get-ChildItem -Path .\Test\*\read*.txt -recurse
    
