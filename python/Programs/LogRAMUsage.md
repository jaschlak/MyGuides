# Program for logging RAM useage

## Code:

    import psutil, os, sys, datetime, time;

    path = os.path.abspath(__file__+'\\..');

    #%% Creates reads config file if it doesn't exist

    filename  = 'Read_Duration.txt';

    if not os.path.exists(filename):
        file=open(filename,"w+");
        file.close();
        
        text = 'How long of an interval between reads (seconds) :\nHow long would you like the code to run (iterations) :'
        
        file= open(filename,"w");
        file.write(text);
        file.close();
        
        sys.exit();
        
    #%% Checks config file for iterations and duration sizes

    file = open(filename,"r");

    iterations = int(file.readline().split(':')[1].strip());
    duration = int(file.readline().split(':')[1].strip());

    file.close();

    #txt_cont

    filename = 'RAMInfo.txt';

    text = '-------------------------------------------------------------------------------\n\n'+ '[' + str(datetime.datetime.now())+']\n\n';

    file= open(filename,"a+");
    file.write(text);
    file.close();

    #%%Cycles through and gathers RAM information

    for i in range(0,duration):

        
        cpu = psutil.cpu_percent();
        
        obj_ram = psutil.virtual_memory();
        
        dict_disk = dict(psutil.disk_io_counters()._asdict())
        
        
        dict_ram = dict(psutil.virtual_memory()._asdict());
        
        pid = os.getpid();
        py = psutil.Process(pid);
        memoryUse = py.memory_info()[0]
        
        
        #%% Check if file exists and create it
        filename = 'RAMInfo.txt';
        
        if not os.path.exists(filename):
            file=open(filename,"w");
            file.close();
        
        #%% Append .txt file
        
        avail = round(dict_ram['available'] * 10**(-9),3);
        tot = round(dict_ram['total'] * 10**(-9),3);
        pyuse = round(memoryUse * 10**(-9),3);
        
        write_count = dict_disk['write_count'];
        write_time = dict_disk['write_time']*10**(-3);
        
        read_count = dict_disk['read_count'];
        read_time = dict_disk['read_time'] * 10**(-3);
        
        
        
        text = '[' + str(datetime.datetime.now())+']\n' + '\nCPU Percent Usage: ' + str(cpu) +'%'+ \
        '\n\nRAM Available: ' + str(avail) + \
        '\nRAM Percent Used: ' + str(dict_ram['percent']) + '%\nRAM Total: ' + str(tot) + \
        '\nRAM Python is using: ' + str(pyuse) + '\n\n'+ \
        'Write Count :' + str(write_count) + '\nWrite Time: ' + str(write_time) + \
        '\n\nRead Count: '+ str(read_count) + '\nRead Time: ' + str(read_time) + '\n\n\n\n';
        
        
        file= open(filename,"a+");
        file.write(text);
        file.close();
        
        time.sleep(iterations);
       
    #%% Adds final page break to show reading is complete
    text = '-------------------------------------------------------------------------------\n\n';

    file= open(filename,"a+");
    file.write(text);
    file.close();

