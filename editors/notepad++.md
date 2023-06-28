# Notepad++

    Usefull things in notepad++
    
## Regex Replace

    ## Split line based on delimiter
    
        search criteria:  (.+?){insert delimiting value}(.+)
        replace criteria: $1{insert replacing value}$2
    
    #   example: replace every first space with a tab

        search criteria:  (.+?)\s(.+)
        replace criteria: $1\t$2