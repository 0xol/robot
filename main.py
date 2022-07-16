from time import sleep
from machine import Pin

button = Pin(0, Pin.IN)


while button.value():
    sleep(0.2)

print("starting")
import line

