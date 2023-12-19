# RAM Useage

    Ways to get RAM Useage info in python
    
# psutil

    float_ram = psutil.cpu_percent()

    obj_ram = psutil.virtual_memory();

    dict_ram = dict(psutil.virtual_memory()._asdict())
    
    #memory used by python file
    pid = os.getpid()
    py = psutil.Process(pid)
    memoryUse = py.memory_info()[0]/2.**30  # memory use in GB...I think