from machine import Pin
import time
from motor import Motor 

     
sens1 = Pin(33, Pin.IN)
sens2 = Pin(32, Pin.IN)
sens3 = Pin(35, Pin.IN)
sens4 = Pin(34, Pin.IN)
led1 = Pin(2, Pin.OUT)

robot = Motor()

def followLeft():
    led1.value(1)
    finish_time = time.time() + 2
    while time.time() < finish_time:
        if sens1.value(): robot.drive(0, -400)
        elif sens2.value(): robot.drive(180, -50)
        elif sens3.value(): robot.drive(180, 50)
    led1.value(0)

def followRight():
    led1.value(1)
    finish_time = time.time() + 2
    while time.time() < finish_time:
        if sens4.value(): robot.drive(0, 400)
        elif sens3.value(): robot.drive(180, 50)
        elif sens2.value(): robot.drive(180, -50)
    led1.value(0)

def followForTime(time_len):
    
    finish_time = time.time() + time_len
    while time.time() < finish_time:
        if sens1.value(): robot.drive(175, -200)
        elif sens2.value(): robot.drive(225, -100)
        if sens4.value(): robot.drive(175, 200)
        elif sens3.value(): robot.drive(225, 100)
    
    
    
robot.drive(250, 0)
followForTime(7.1)
followRight()
followForTime(9)
followLeft()
followForTime(10)
robot.stop()