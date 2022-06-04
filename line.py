from machine import Pin
import time
from motor import Motor 

     
sens1 = Pin(33, Pin.IN)
sens2 = Pin(32, Pin.IN)
sens3 = Pin(35, Pin.IN)
sens4 = Pin(34, Pin.IN)

robot = Motor()


finish_time = time.time() + 5
robot.drive(200, 0)
while time.time() < finish_time:
    if sens1.value(): robot.drive(150, -100)
    elif sens2.value(): robot.drive(180, -50)
    if sens4.value(): robot.drive(150, 100)
    elif sens3.value(): robot.drive(180, 50)
    
robot.stop()