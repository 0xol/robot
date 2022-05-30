from machine import Pin


class Sensed:
  
  def __init__(self, sen1=33, sen2=32, sen3=35, sen4=34):     
    self.sens1 = Pin(sen1, Pin.IN)
    self.sens2 = Pin(sen2, Pin.IN)
    self.sens3 = Pin(sen3, Pin.IN)
    self.sens4 = Pin(sen4, Pin.IN)
    
  def values(self):
    self.s1 = self.sens1.value()
    self.s2 = self.sens2.value()
    self.s3 = self.sens3.value()
    self.s4 = self.sens4.value()
    return self.s1, self.s2, self.s3, self.s4
    
  def sense1(self):
    if self.sens1.value(1) == True:
      self.sensed1 = True
    elif self.sens1.value(1) /= True:
      self.sensed1 = False
    return self.sensed1
    
  def sense2(self):
    if self.sens2.value(1) == True:
      self.sensed2 = True
    elif self.sens2.value(1) /= True:
      self.sensed2 = False
    return self.sensed2
  
  def sense3(self):
    if self.sens3.value(1) == True:
      self.sensed3 = True
    elif self.sens3.value(1) /= True:
      self.sensed3 = False
    return self.sensed3
  
  def sense4(self):
    if self.sens4.value(1) == True:
      self.sensed4 = True
    elif self.sens4.value(1) /= True:
      self.sensed4 = False
    return self.sensed4
             
             
