# Multi-Threading

    Collection of generic multi-threading examples for reference
    
## Example 1: Home Made thread pool (keep a determined number of threads alive at all times):

    import time
    import threading
    import keyboard

    def thread_1(i):
        time.sleep(2)
        print("Number of active threads:", threading.active_count())
        print('Value by Thread 1:', i)

    def thread_2(i):
        time.sleep(5)
        print("Number of active threads:", threading.active_count())
        print('Value by Thread 2:', i)
        
    def thread_3(i):
        print("Number of active threads:", threading.active_count())
        print("Value by Thread 3:", i)
        
    # Creating sample threads 
    thread1 = threading.Thread(target=thread_1, args=(1,))
    thread2 = threading.Thread(target=thread_2, args=(2,))
    thread3 = threading.Thread(target=thread_3, args=(3,))

    print("Number of active threads in the starting:", threading.active_count())
    print("The active threads in the starting is 1 which is the main thread that executes till the program runs")

    # Starting the threads
    thread1.start()
    thread2.start()
    thread3.start()


    mentioned = False

    while True:
        
        # just using thread 2 for concept
        if threading.active_count() < 10 and mentioned == False:
            thread2.start()
            print('Adding 1 more')
            print(threading.active_count())
            mentioned = True
        

        if keyboard.is_pressed('z'):
            break