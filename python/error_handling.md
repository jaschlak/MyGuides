# Error Handling

    How to detect error type and explicitly handle it
    
print('\n\n\nExample 1: Detecting Error Type')
# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)



print('\n\n\nExample 2: Handling Explicit Errors')

randomList = ['a', 0, 2]

for entry in randomList:
    try:
       print("The entry is", entry)
       r = 1/int(entry)
       break
    
    except ValueError:
       print('ValueError Detected')
       pass
    
    except (ZeroDivisionError):
       # handle multiple exceptions
       # TypeError and ZeroDivisionError
       print('ZeroDivisionError detected')
       pass
    
    except Exception as e:
       print('Random error detected')
       pass