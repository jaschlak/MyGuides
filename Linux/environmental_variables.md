# Environmental Variables

    Environmental variable commands
    
## Create Environmental Variable (temperary)

    export <variableName>=<variableValue>
    
## Create Environmental Variable (persistent)

    set | head -n 1                         # find shell path being used for used
    
    nano <bash path>                        # add temperary command to this file (export <variableName>=<variableValue>)
    
    nano ~:.profile                         # add command to .profile to activate environmental variable for cronjob
    
## Remove Environmental Variable

    set | head -n 1                         # find shell path being used for used
    
    nano <bash path>                        # remove environmental variable from users bash
    
    nano ~:.profile                         # remove environmental variable from users profile for cron
    
## Print Environmental Variable
    
    printenv <variableName>
    
## Print all Environmental Variables

    printenv 
    
## Find shell being used for user

    set
    
## Find shell version being used

    echo $BASH_VERSION
    