
sheapsz = [5,7,300,90,24,50,75]
print("My sheap size",sheapsz)
for i in range(3):
    print("month",i)
    print("now here is my flock",sheapsz)
    a = sheapsz.index(max(sheapsz))
    print("biggest sheap :",max(sheapsz))
    sheapsz[a] = 8
    print("after shararing here is my flock",sheapsz)
    b =[50,50,50,50,50,50,50]
    sheapsz = [sum(x) for x in zip(sheapsz,b)]
print("month 3:" )       
print("now here is my flock", sheapsz)
b=sum(sheapsz)
print("my flock has size in total: ",b)
print("i would get: ",b*2,"$")
    
    
