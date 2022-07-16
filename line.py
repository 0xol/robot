from machine import Pin, I2C
import time
from motor import Motor
from servo import Servo
from vl53l0x import VL53L0X

i2c = I2C(1)

dis_sens = VL53L0X(i2c)

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
        if sens1.value(): robot.drive(175, -100)
        elif sens2.value(): robot.drive(225, -50)
        if sens4.value(): robot.drive(175, 100)
        elif sens3.value(): robot.drive(225, 50)
    
def followForDistance(distance):
    
    while dis_sens.read() > distance:
        
        if sens1.value(): robot.drive(175, -100)
        elif sens2.value(): robot.drive(225, -50)
        if sens4.value(): robot.drive(175, 100)
        elif sens3.value(): robot.drive(225, 50)
        
        dis_sens.read()
    
    robot.stop()

def drop():
    
    Servo.set_servo(180)
    sleep(5)
    Servo.set_servo(90)
    
robot.drive(400, 0)
followForTime(10)
followRight()
followForTime(14)
followLeft()
followForDistance(100)
drop()
robot.stop()