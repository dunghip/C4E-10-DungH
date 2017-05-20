from turtle import*
import time
begin_fill
color("blue","blue")
def  draw_square(a,color):
    begin_fill
    for i in range(4):
        fd(a)
        left(90)
    end_fill()
draw_square(200,100)
    


    

for i in range(30):
    draw_square(i * 5,"red")
    left(17)
    penup()
    forward(i * 2)
    pendown()
       
draw_square(color)
