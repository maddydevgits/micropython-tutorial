from machine import *
import urequests 
import network 
import time 
from dht import *

dht_pin=Pin(2,Pin.IN)
sensor=DHT22(dht_pin)

THINGSPEAK_WRITE_API_KEY = '' 


# HTTP Headers 
HTTP_HEADERS = {'Content-Type': 'application/json'}
UPDATE_TIME_INTERVAL = 500 # in ms 

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('Wokwi-GUEST', '')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

do_connect()
while True:
    try:
        sensor.measure()
        temp=sensor.temperature()
        hum=sensor.humidity()

        print('Temperature: ',temp)
        print('Humidity: ',hum)

        sensor_data={
            'field1': hum,
            'field2':temp
        }
        request = urequests.post( 
            'http://api.thingspeak.com/update?api_key=' + THINGSPEAK_WRITE_API_KEY, 
            json=sensor_data, 
            headers=HTTP_HEADERS 
        ) 
        request.close() 
    except OSError as e:
        print('Failed to read sensor')
     
    except Exception as e: 
        print("Failed to send data:", e) 
    print(sensor_data) 
