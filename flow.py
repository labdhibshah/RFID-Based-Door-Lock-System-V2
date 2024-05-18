from rfid import *
from verify import *
from sheets import *
from servo import *

A = Rfidread()
print(A)

B = verify_num(A)
print(B)
updatesheet(A, B)
if B == True:
    move_servo()
    



