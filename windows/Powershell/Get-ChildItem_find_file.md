# Get-ChildItem

	This will search for files in useful ways
	
## Recursive Example

	# structure
	Get-ChildItem .\<known_folder>\*\<part_file>*.<ext> -recurse
	
	# example
	Get-ChildItem .\Test\*\read*.txt -recurse