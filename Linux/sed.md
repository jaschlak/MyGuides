# sed

    sed is a great tool to find and replace information
    
## Find string match from regex (start and finish) accross multiple lines

    sed -n '/<start string>/,/<end string>/p' <filename>