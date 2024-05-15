from machine import *
from time import *

a=Pin(35,Pin.IN)

while True:
    if a.value()==0:
        while a.value()==0:
            pass
        print ('Pressed')
        sleep(0.01)
