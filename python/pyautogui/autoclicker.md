# AutoClicker

	This is an autoclicker for games
	
## Version 1

	import pyautogui
	import keyboard
	import time

	time.sleep(3)

	for i in range(0,10000):
		
		if keyboard.is_pressed('m'):
			#print('m detected button pressed')
			break

		pyautogui.click() 