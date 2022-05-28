from machine import Pin
from time import sleep

#sens1 = D33
#sens2 = D32
#sens3 = D35
#sens4 = D34

sens1 = Pin(33, Pin.IN)
sens2 = Pin(32, Pin.IN)
sens3 = Pin(35, Pin.IN)
sens4 = Pin(34, Pin.IN)



while(1):
    print(sens1.value(), sens2.value(), sens3.value(), sens4.value())
    
    sleep(1)