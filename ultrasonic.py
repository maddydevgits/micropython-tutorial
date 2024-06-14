import machine
import time

# Set up the HC-SR04 sensor
trigger_pin = machine.Pin(5, machine.Pin.OUT)
echo_pin = machine.Pin(18, machine.Pin.IN)

def measure_distance():
    # Send a 10us pulse to trigger the measurement
    trigger_pin.off()
    time.sleep_us(2)
    trigger_pin.on()
    time.sleep_us(10)
    trigger_pin.off()

    # Measure the duration of the echo pulse
    while echo_pin.value() == 0:
        pulse_start = time.ticks_us()
    while echo_pin.value() == 1:
        pulse_end = time.ticks_us()

    pulse_duration = time.ticks_diff(pulse_end, pulse_start)
    distance = (pulse_duration * 0.0343) / 2  # Convert to cm

    return distance

while True:
    try:
        distance = measure_distance()
        print('Distance: {:.2f} cm'.format(distance))
    except Exception as e:
        print('Failed to read sensor:', e)
    
    time.sleep(1)
