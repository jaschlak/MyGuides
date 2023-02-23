# top

    useful top command examples
    
## examples

    -- normal
    top -b -n 1
    
    -- filter by ram and output a reasonable amount of lines
    top -b -n 1 | head -n 15
    
    -- filter for specific process and addup cpu/ram
    top -b -n 1 | grep <process_name_filter> | awk '{cpu+=\$9; mem=\$10} END {print \"<process_display> CPU: \" cpu \" Mem: \"  mem}'
    