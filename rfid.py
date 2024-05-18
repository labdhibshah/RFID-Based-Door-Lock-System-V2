import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import verify as v

reader = SimpleMFRC522()

print("Hold a card near the reader...")

# Wait for a card to be scanned
id, data = reader.read()
def Rfidread():
    return id

# if v.verify_num(id) == True:
#     print('Rachu thank you')

    
GPIO.cleanup()
GPIO.setwarnings(False)
