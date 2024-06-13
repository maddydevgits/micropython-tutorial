from machine import *
from dht import *
import time

dht_pin=Pin(2,Pin.IN)
sensor=DHT22(dht_pin)

while True:
    try:
        sensor.measure()
        temp=sensor.temperature()
        hum=sensor.humidity()

        print('Temperature: ',temp)
        print('Humidity: ',hum)
    except OSError as e:
        print('Failed to read sensor')
    
    time.sleep(2)
