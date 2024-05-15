from machine import *
from time import *

a=Pin(35,Pin.IN)
b=Pin(2,Pin.OUT)
count=0

while True:
    if a.value()==0:
        while a.value()==0:
            pass
        count+=1
        print ('Pressed and Count: ',count)
        if count%2==0:
            b.value(0)
        else:
            b.value(1)
        sleep(0.01)
    
    
