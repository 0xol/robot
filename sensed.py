from machine import Pin


class Sensed:
  
  def __init__(self, sen1=33, sen2=32, sen3=35, sen4=34):
               
    self.sens1 = Pin(sen1, Pin.IN)
    self.sens2 = Pin(sen2, Pin.IN)
    self.sens3 = Pin(sen3, Pin.IN)
    self.sens4 = Pin(sen4, Pin.IN)
    
  def sense1(self):
    if self.sens1.value(1) == True:
      self.sense1 = True
    elif self.sens1.value(1) /= True:
      self.sense1 = False
    return self.sense1
    
  def sense2(self):
    if self.sens2.value(1) == True:
      self.sense2 = True
    elif self.sens2.value(1) /= True:
      self.sense2 = False
    return self.sense2
  
  def sense3(self):
    if self.sens3.value(1) == True:
      self.sense3 = True
    elif self.sens3.value(1) /= True:
      self.sense3 = False
    return self.sense3
  
  def sense4(self):
    if self.sens4.value(1) == True:
      self.sense4 = True
    elif self.sens4.value(1) /= True:
      self.sense4 = False
    return self.sense4
             
             
