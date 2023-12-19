# Keyboard Detect

    This catches multiple keystrokes to perform an action
    
## Simple Code

import keyboard

    while True:
        
        if keyboard.is_pressed('w'):
            print('You pressed w!!!')
            
        if keyboard.is_pressed('q'):
            print('you pressed q!!!')
            
        if keyboard.is_pressed('z'):
            break