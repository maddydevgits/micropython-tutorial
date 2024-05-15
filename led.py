from machine import *
from time import *

b=Pin(2,Pin.OUT)

while True:
    b.value(1)
    sleep(0.5)
    b.value(0)
    sleep(0.5)
    
    
