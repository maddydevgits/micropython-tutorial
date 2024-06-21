import machine
import utime

# Set up the servo pin as an output
servo_pin = machine.Pin(16, machine.Pin.OUT)

# Create a PWM object for the servo pin
pwm = machine.PWM(servo_pin, freq=50)

def set_servo_angle(angle):
    # Calculate the duty cycle for the servo based on the angle
    duty_cycle = int(((angle / 180) * 2 + 0.5) / 20 * 1023)
    # Set the duty cycle for the servo
    pwm.duty(duty_cycle)

while True: 
    # Set the servo to a specific angle
    set_servo_angle(0)

    # Wait for a second
    utime.sleep(1)

    # Set the servo to a different angle
    set_servo_angle(180)

    # Wait for a second
    utime.sleep(1)
