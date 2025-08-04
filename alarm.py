import pygame
import datetime
import time
import random

a= random.randint(1,100)
b=random.randint(1,100)

pygame.mixer.init()
pygame.init()
sound = pygame.mixer.Sound("bird-flight-236928.mp3")

def set_alarm():
    global user_alarm
    user_alarm=input(f"Enter your alarm date time (Y-M-D , hr:min)")
    user_alarm=datetime.datetime.strptime(user_alarm,"%Y-%m-%d , %H:%M")
    print("you set an alarm at " ,end=" " )
    print(user_alarm)
    

set_alarm()
while True :
  current_time=datetime.datetime.now()
  print(current_time.strftime("%H:%M:%S"), end='\r')
  time.sleep(1)

  if current_time > user_alarm :
     sound.play()
     print("\nwake up ! 😴")
     while True :
        c=int(input(f"{a} + {b} = " ))
        if a+b == c :
           break
     break
 
  

