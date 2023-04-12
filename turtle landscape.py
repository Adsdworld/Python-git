from turtle import * 
from random import randint 
Line=0
bgcolor('black') 
speed(0) 

for i in range(Line+1):
 goto(-400, (200+1-i))
 r = randint(0,255) 
 g = randint(0,255)  
 b = randint(0,255) 
  
 colormode(255)  
 pencolor(r,g,b) 
 down()
 fd(800)
 up()
  
exitonclick() 