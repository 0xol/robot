from machine import Pin
from time import sleep, time
from motor import Motor
from sensed import Sensed

#sensor1 = D33
#sensor2 = D32
#sensor3 = D35
#sensor4 = D34

sens1 = Pin(33, IN)
sens2 = Pin(32, IN)
sens3 = Pin(35, IN)
sens4 = Pin(34, IN)

robot = Motor()
s = Sensed()

time_allowed = 180
start_time = time()
last_time = start_time
best_time = 0
laps = 0
#times for timer and laps for lap count

start = True
driving = False
turning_around = False
returning = False
intersection1 = False
intersection2 = False
end = False
restarting = False
#sections of track

while end == False:

    while restarting = True:
        robot.drive(1, 90)
        sleep(1)
        
        if s.sense1 or s.sense2 or s.sense3 or s.sense4 == True:
            robot.drive(300, 0)
            sleep(0.1)
            
            if s.sense1 or s.sense2 or s.sense3 or s.sense4 == True:
                driving = True
                restarting = False
                
            else: 
                robot.drive(-300, 0)
    #turns around and starts again
    
    while start == True:
        robot.drive(300, 0)
        sleep(0.1)
        if s.sense1 and s.sense2 and s.sense3 and s.sense4 /= True:
            start = False
            driving = True
    #starts the track
    
    while turning_around == True:
        robot.drive(1, 90)
        sleep(1)
        
        if s.sense1 or s.sense2 or s.sense3 or s.sense4 == True:
            robot.drive(300, 0)
            sleep(0.1)
            
            if s.sense1 or s.sense2 or s.sense3 or s.sense4 == True:
                turning_around = False
                returning = True
                
            else: 
                robot.drive(-300, 0)
                sleep(0.1)
    #turns around after reaching the tower
    
    while driving or returning == True:
        
        print(s.values)

        if s.sense1 and s.sense2 and s.sense3 and s.sense4 == True:
            if driving == True:
                robot.drive(1, 90)
                sleep(0.1)
                
                if s.sense1 and s.sense3 or s.sense2 and s.sense4 == True:
                    driving = False
                    turning_around = True
        
            elif returning == True:
                if intersection1 == False:
                    robot.drive(300, 90)
                    sleep(1)
                   
                    if s.sense1 or s.sense2 or s.sense3 or s.sense4 == True:
                        intersection1 = True
                    
                elif intersetion2 == False:
                    robot.drive(300, -90)
                    sleep(1)
                    
                    if s.sense1 or s.sense2 or s.sense3 or s.sense4 == True:
                        intersection2 = True
                #fix if turns wrong way or too far/fast
                
                elif intersection2 == True:
                    robot.drive(1, 90)
                    sleep(0.1)
                
                    if s.sense1 and s.sense3 or s.sense2 and s.sense4 == True:
                        returning = False
                        intersection1 = False
                        intersection2 = False
                        end = True
        #checks to see if at tower, end or an intersection
        
        elif s.sense1 and s.sense2 == True:
            robot.drive(300, -90)
            sleep(1)
            
        elif s.sense3 and s.sense4 == True:
            robot.drive(300, 90)
            sleep(1)
        
        elif s.sense1 == True:
            robot.drive(300, -45)
            
        elif s.sense4 == True:
            robot.drive(300, 45)
            
        elif s.sense2 == True:
            robot.drive(300, -20)
            
        elif s.sense3 == True:
            robot.drive(300, 20)
        #general line following     
        #may need to adjust values
        
if end == True:
laps += 1
print("The robot has completed another lap.")
#counts number of laps

total_time = round((time() - start_time), 2)
lap_time = round((time() - last_time), 2)
last_time = time()
#gets time values

if lap_time < best_time:
    best_time = lap_time
    
if total_time < time_allowed
    time_left = time_allowed - total_time
    print("There is " + time_left + " seconds left until end.")
    
    if time_left > 10
        restarting = True
        end = False
        
    elif time_left < 10
        print("The robot cannot complete a full lap within the time limit.")
        restarting = True
        end = False
#checks if another lap has a chance of being completed
        
elif total_time - start_time > time_allowed
    print("The robot has run out of time to run laps.")
    print()
    print("The robot completed " + laps + " laps.")
    print("The robot's fastest time was: " + best_time + " seconds.")
    
            
            
            
            
            
    
