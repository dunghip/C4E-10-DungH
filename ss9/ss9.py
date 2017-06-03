import pygame
from  math import  sqrt

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distant(self,a):
        self.distant = sqrt((a.x - self.x)**2+(a.y - self.y)**2)


    def halfway(self,a):
        self.half_x = (self.x + a.x)/2
        self.half_y = (self.y + a.y)/2
        return (self.half_x, self.half_y)

    def reflect(self):
        self.reflect_x = (self.x, -self.y)
        self.reflect_y = (-self.x, self.y)
        return (self.reflect_x, self.reflect_y)

    def reflect_origin(self):
        self.reflect_origin = (-self.x, -self.y)
        return (self.reflect_origin)

    # def get_line_to(self,a):

a = Point(2, 1)
b = Point(10, 9)
distant = b.distant(a)
half_x,half_y = a.halfway(b)
reflect_x = a.reflect()
reflect_y = a.reflect()
reflect_origin = a.reflect()

print("trung diem: ({0},{1})".format(half_x , half_y))
print("khoang cach giua 2 diem la:{0}".format(distant))
print("doi xung qua0x:{0},doi xung qua 0y:{1},doi xung qua 0:{2}".format(reflect_x,reflect_y,reflect_origin))
