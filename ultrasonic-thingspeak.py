import machine 
import urequests 
import network 
import time 

# Wi-Fi Credentials 

ssid = 'Wokwi-GUEST' 
password = '' 

# ThingSpeak API Key 

THINGSPEAK_WRITE_API_KEY = 'RR82FJY6IM1F26V6' 


# HTTP Headers 
HTTP_HEADERS = {'Content-Type': 'application/json'} 


# Update Interval 
UPDATE_TIME_INTERVAL = 500 # in ms 

 
# Ultrasonic Sensor Pins 

trigger_pin = 5 
echo_pin = 18 

# Wi-Fi Connection 

def connect_wifi(ssid, password): 
    sta_if = network.WLAN(network.STA_IF) 
    sta_if.active(True) 
    if not sta_if.isconnected(): 
        print('Connecting to network...') 
        sta_if.connect(ssid, password) 
        while not sta_if.isconnected(): 
            pass 
    print('Network config:', sta_if.ifconfig()) 

 
# Read Distance from Ultrasonic Sensor 
def read_distance(trigger_pin, echo_pin): 
    trigger = machine.Pin(trigger_pin, machine.Pin.OUT) 
    echo = machine.Pin(echo_pin, machine.Pin.IN) 
 
    # Trigger the sensor 
    trigger.off() 
    time.sleep_us(2) 
    trigger.on() 
    time.sleep_us(10) 
    trigger.off() 

    # Measure the duration of the echo pulse 
    while echo.value() == 0: 
        pass 
    start = time.ticks_us() 
    while echo.value() == 1: 
        pass 
    end = time.ticks_us() 
    duration = time.ticks_diff(end, start) 
 
    # Calculate the distance in centimeters 
    distance = (duration / 2) / 29.1 
    return distance 

# Connect to Wi-Fi 
connect_wifi(ssid, password) 
 
while True: 
    # Read Ultrasonic Sensor Data 
    distance = read_distance(trigger_pin, echo_pin) 
    # Prepare Data for ThingSpeak 
    sensor_data = { 
        'field1': distance 
    } 
    # Post Data to ThingSpeak 
    try: 
        request = urequests.post( 
            'http://api.thingspeak.com/update?api_key=' + THINGSPEAK_WRITE_API_KEY, 
            json=sensor_data, 
            headers=HTTP_HEADERS 
        ) 
        request.close() 
    except Exception as e: 
        print("Failed to send data:", e) 
    print(sensor_data) 
    # Wait for the update interval before reading again 
    time.sleep_ms(UPDATE_TIME_INTERVAL) 
