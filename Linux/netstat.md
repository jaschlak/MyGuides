# netstat

    Useful examples of netstat
    
## examples

    -- general, no dns lookup, 
    netstat -an
    
    -- see all unique ip/ports and a count
    netstat -an | awk '{print $5}' | grep :$port | sort -n | uniq -c | sort -nr