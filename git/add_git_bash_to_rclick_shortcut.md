# Add Git BASH to Shortcut

	Add Git BASH to right click shortcut menu
	
## Step 1: make file

	Make File called "OpenGitBash.reg"
	
## Step 2: add contents to file

	Windows Registry Editor Version 5.00
	; Open files
	; Default Git-Bash Location <path to git-bash.exe>

	[HKEY_CLASSES_ROOT\*\shell\Open Git Bash]
	@="Open Git Bash"
	"Icon"="<path to git-bash.exe>"

	[HKEY_CLASSES_ROOT\*\shell\Open Git Bash\command]
	@="\"<path to git-bash.exe>\" \"--cd=%1\""

	; This will make it appear when you right click ON a folder
	; The "Icon" line can be removed if you don't want the icon to appear

	[HKEY_CLASSES_ROOT\Directory\shell\bash]
	@="Open Git Bash"
	"Icon"="<path to git-bash.exe>"


	[HKEY_CLASSES_ROOT\Directory\shell\bash\command]
	@="\"<path to git-bash.exe>\" \"--cd=%1\""

	; This will make it appear when you right click INSIDE a folder
	; The "Icon" line can be removed if you don't want the icon to appear

	[HKEY_CLASSES_ROOT\Directory\Background\shell\bash]
	@="Open Git Bash"
	"Icon"="<path to git-bash.exe>"

	[HKEY_CLASSES_ROOT\Directory\Background\shell\bash\command]
	@="\"<path to git-bash.exe>\" \"--cd=%v.\""
	