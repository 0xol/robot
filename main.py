from machine import Pin
from time import sleep, time
from motor import Motor
from sensed import Sensed

#sensor1 = D33
#sensor2 = D32
#sensor3 = D35
#sensor4 = D34

robot = Motor()

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
        
        if sense1 or sense2 or sense3 or sense4 == True:
            robot.drive(300, 0)
            sleep(0.1)
            
            if sense1 or sense2 or sense3 or sense4 == True:
                driving = True
                restarting = False
                
            else: 
                robot.drive(-300, 0)
    #turns around and starts again
    
    while start == True:
        robot.drive(300, 0)
        sleep(0.1)
        if sense1 and sense2 and sense3 and sense4 /= True:
            start = False
            driving = True
    #starts the track
    
    while turning_around == True:
        robot.drive(1, 90)
        sleep(1)
        
        if sense1 or sense2 or sense3 or sense4 == True:
            robot.drive(300, 0)
            sleep(0.1)
            
            if sense1 or sense2 or sense3 or sense4 == True:
                turning_around = False
                returning = True
                
            else: 
                robot.drive(-300, 0)
                sleep(0.1)
    #turns around after reaching the tower
    
    while driving or returning == True:
        
        print(sens1.value(), sens2.value(), sens3.value(), sens4.value()

        if sense1 and sense2 and sense3 and sense4 == True:
            if driving == True:
                robot.drive(1, 90)
                sleep(0.1)
                
                if sense1 and sense3 or sense2 and sense4 == True:
                    driving = False
                    turning_around = True
        
            elif returning == True:
                if intersection1 == False:
                    robot.drive(300, 90)
                    sleep(1)
                    
                elif intersetion2 == False:
                    robot.drive(300, -90)
                    sleep(1)
                #fix if turns wrong way
                
                elif intersection2 == True:
                    robot.drive(1, 90)
                    sleep(0.1)
                
                    if sense1 and sense3 or sense2 and sense4 == True:
                        returning = False
                        intersection1 = False
                        intersection2 = False
                        end = True
        #checks to see if at tower, end or an intersection
        
        elif sense1 and sense2 == True:
            robot.drive(300, -90)
            sleep(1)
            
        elif sense3 and sense4 == True:
            robot.drive(300, 90)
            sleep(1)
        
        elif sense1 == True:
            robot.drive(300, -45)
            
        elif sense4 == True:
            robot.drive(300, 45)
            
        elif sense2 == True:
            robot.drive(300, -20)
            
        elif sense3 == True:
            robot.drive(300, 20)
        #general driving
        
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
    
            
            
            
            
            
    
