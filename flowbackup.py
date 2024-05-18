#Importing libraries
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from gpiozero import Servo
from time import sleep
import pigpio
from verify import *

# Create an instance of the SimpleMFRC522 class

reader = SimpleMFRC522()
servo = 20
pwm = pigpio.pi()
pwm.set_mode(servo, pigpio.OUTPUT)
pwm.set_PWM_frequency( servo, 50 )


print("Hold a card near the reader...")

# Wait for a card to be scanned
id, data = reader.read()

# Print the ID and data on the card
print("Card ID: {}".format(id))

if verify_num(id) == True:
    print("You are Authorized")

if id == 389276073774:
    print("Name: Labdhi shah u can enter now!")
    sleep(0.5)
    pwm.set_servo_pulsewidth( servo, 500 ) ;#0 degree
    sleep(0.5)
    pwm.set_servo_pulsewidth( servo, 1500 ) ;#90 degree
    sleep(3.5)
    pwm.set_servo_pulsewidth( servo, 500 ) ;#0 degree

else:
    print("sorry u r not authorized")

GPIO.cleanup()
GPIO.setwarnings(False)
