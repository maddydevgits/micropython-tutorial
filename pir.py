import machine
import time

# Set up the PIR sensor on GPIO 14
pir_pin = machine.Pin(14, machine.Pin.IN)

while True:
    if pir_pin.value() == 1:
        print('Motion detected!')
    else:
        print('No motion detected.')
    
    time.sleep(1)
