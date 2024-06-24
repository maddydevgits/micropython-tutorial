from network import *
from machine import *
from time import *
import urequests
import ujson

led=Pin(2,Pin.OUT)

api='https://api.thingspeak.com/channels/2584001/fields/1.json?results=1'

def connectWiFi():
    sta=WLAN(STA_IF)
    if not sta.isconnected():
        sta.active(True)
        sta.connect('Wokwi-GUEST','')
        while not sta.isconnected():
            pass
    print('WiFi Connected')

connectWiFi()
while True: # infinite loop
    response=urequests.get(api) # calling api
    if response.status_code==200: # success
        doc=response.content # bytes format
        doc=doc.decode('utf-8') # decoding bytes into string (chars)
        doc=ujson.loads(doc) # string into json
        doc=doc['feeds'][0] # dictionary - feeds, list of feeds
        doc=doc['field1'] # extracting field1
        doc=int(doc) # str into int
        if doc>0:
            led.on()
        elif doc<=0:
            led.off()
        print(doc)
    sleep(2)
