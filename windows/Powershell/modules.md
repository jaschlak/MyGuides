# Powershell Modules

    How to interact with install modules in powershell
    
## Commnads

    $env:PSModulePath                                           # path list for installed modules
    
    Import-Module <module_path>.psm1                            # after import you can call functions defined in module, note: if drop in PSModulePath, just filename
    Import-Module <filename>.psm1                               # if file is in the a $env:PSModulePath, you just need to import the filename (also needs to be in folder of same name)
    
    
    
    
    
## Example

# Be Nice Example

    ## folder structure %env:PSModulePath[0] -> benice -> benice.psm1

    function benice()
    {
        $nicearray = @(
            "You are beautiful",
            "You are smart",
            "You're outfit looks nice today",
            "I like your style",
            "You're strong",
            "You can do this",
            "You are brave",
            "You have the courage of your convictions",
            "Colors seem brighter when you're around",
            "You're a candle in the darkness",
            "You're someone's reason to smile",
            "You're a great listener",
            "You're so thoughtful",
            "Your perspective is refreshing",
            "You could survive a zombie apocalypse"
        )

        $randIndex = Get-Random -Minimum 0 -Maximum $nicearray.COUNT
        WRITE-OUTPUT $nicearray[$randIndex]

    }
    
    #run above module after placement
    $PSbash> Import-Module benice
    $PSbash> benice