from machine import Pin, PWM

class Motor:
    def __init__(self, ain1=27, ain2=15, apwm=4, bin1=14, bin2=12, bpwm=13):
        
        self.ain1_pin = Pin(ain1, Pin.OUT)
        self.ain2_pin = Pin(ain2, Pin.OUT)
        self.apwm_pin = PWM(Pin(apwm, Pin.OUT), freq=40000, duty=0)
        
        self.bin1_pin = Pin(bin1, Pin.OUT)
        self.bin2_pin = Pin(bin2, Pin.OUT)
        self.bpwm_pin = PWM(Pin(bpwm, Pin.OUT), freq=40000, duty=0)
        
    def right(self, speed):
        if speed == 0:
            self.ain1_pin.value(1)
            self.ain2_pin.value(1)
            
        elif speed > 0:
            self.ain1_pin.value(0)
            self.ain2_pin.value(1)
            if speed > 1023: speed = 1023
            self.apwm_pin.duty(speed)
        
        else:
            self.ain1_pin.value(1)
            self.ain2_pin.value(0)
            speed *= -1
            if speed > 1023: speed = 1023
            self.apwm_pin.duty(speed)
            
        
 
    def left(self, speed):
        if speed == 0:
            self.bin1_pin.value(1)
            self.bin2_pin.value(1)
            
        elif speed < 0:
            self.bin1_pin.value(0)
            self.bin2_pin.value(1)
            speed *= -1
            if speed > 1023: speed = 1023
            self.bpwm_pin.duty(speed)
            
        else:
            self.bin1_pin.value(1)
            self.bin2_pin.value(0)
            if speed > 1023: speed = 1023
            self.bpwm_pin.duty(speed)
    
    def stop(self):
        self.right(0)
        self.left(0)

    def drive(self, forward, steer):
        self.right(forward-steer)
        self.left(forward+steer)
