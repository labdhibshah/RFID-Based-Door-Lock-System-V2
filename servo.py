import pigpio
import RPi.GPIO as GPIO
from time import sleep

servo = 20
pwm = pigpio.pi()
pwm.set_mode(servo, pigpio.OUTPUT)
pwm.set_PWM_frequency( servo, 50 )

# Check if pigpio connection is successful
if not pwm.connected:
    print("Error: Could not connect to pigpio")
    exit()
def move_servo():
    pwm.set_servo_pulsewidth( servo, 500 ) ;#0 degree
    sleep(0.5)
    pwm.set_servo_pulsewidth( servo, 1500 ) ;#90 degree
    sleep(3.5)
    pwm.set_servo_pulsewidth( servo, 500 ) ;#0 degree

