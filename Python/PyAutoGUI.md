# PyAutoGUI

    This is meant to be a reference for usefull PyAutoGUI
    
## Mouse

    pyautogui.moveTo(x, y, duration=num_seconds)                # move mouse to absolute values
    pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)   # move mouse to relative values
    
    pyautogui.dragTo(x, y, duration=num_seconds)                # drag mouse with absolute values
    pyautogui.dragRel(xOffset, yOffset, duration=num_seconds)   # drag mouse with relative values

    pyautogui.position()                                        # gets mouse position
    pyautogui.click(x=3385, y=150)                              # click mouse at location (seems to be limited to 1 screen)
    pyautogui.doubleClick(x=1032, y=63)                         # double click mouse
    pyautogui.rightClick(x=moveToX, y=moveToY)                  # right click    
    pyautogui.middleClick(x=moveToX, y=moveToY)                 # middle click
    pyautogui.tripleClick(x=moveToX, y=moveToY)                 # tripple click
    pyautogui.scroll(amount_to_scroll, x=moveToX, y=moveToY)    # scroll
    
## Keyboard
    pyautogui.typewrite('Hello World')                          # type things
    
## Locate

    locateOnScreen(<insert image in local dir>)                 # locate the position of an image on screen
    pyautogui.locateAllOnScreen(<insert image in local dir>)    # locate center of something using an image on screen
    list(pyautogui.locateAllOnScreen('looksLikeThis.png'))      # list all items on screen that match the image provided    
    
## Wait

    pyautogui.PAUSE = 2.5
    
## Messages

    pyautogui.alert('This displays some text with an OK button.')
    pyautogui.confirm('This displays text and has an OK and Cancel button.')
    pyautogui.prompt('This lets the user type in a string and press OK.')
    
## Screenshot

    pyautogui.screenshot()                                      # returns a Pillow/PIL Image object
    pyautogui.screenshot('foo.png')                             # returns a Pillow/PIL Image object, and saves it to a file
    
## FYI

    When fail-safe mode is True, moving the mouse to the upper-left will raise a pyautogui.FailSafeException that can abort your program:
    pyautogui.FAILSAFE = True
    
## More Documentation:

    https://pyautogui.readthedocs.io/en/latest/mouse.html