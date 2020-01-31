# Python code for keylogger 
# to be used in windows 

import os;
import pyfirmata
import time

board = pyfirmata.Arduino('COM3')
it = pyfirmata.util.Iterator(board)
it.start()

check = True

analog_input = board.get_pin('a:0:i')
while check == True:
    analog_value = analog_input.read()
    print(analog_value)
    try:
        if analog_value < 0.001:
            os.system("rundll32.exe user32.dll,LockWorkStation")
            exit()
            time.sleep(0.1)
            check = False
            break
    except:
        print('Ruh Roh')
    







