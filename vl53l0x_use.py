from vl53l0x import VL53L0X
from machine import I2C, Pin
import time

I2C_bus = I2C(1)

distance_sensor = VL53L0X(I2C_bus)

while True:
    print(distance_sensor.read())
    time.sleep(0.1)