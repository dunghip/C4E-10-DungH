from turtle import *
 
shape("turtle")
speed(-1)
 
 
for i in range(3,7):
    for _ in range (i):
        forward(100)
        left(360/i)
