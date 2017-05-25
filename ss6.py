#box-pusher
#map
#box
#destination

#set pusher ccoordinate
#rep: P
pusher_x = 1
pusher_y = 0

#set box coordinate
#rep: B

boxes =[
    {
        "x":3,
        "y":2
    },
    {
        "x":1,
        "y":3
    }
        ]
#set destonation coordinate
#rep: D
dests= [
    {
        "x":2,
        "y":3
        
    },
    {
        "x":3,
        
        "y":6
    }
    ]


#set map size
size_x = 6
size_y = 6

def check_overlap(x,y,items):
    for item in items:
        if x == item["x"] and y == item["y"]:
            return True
    return False


def is_in_map(x,y,size_x,size_y):
    if 0<= x < size_x and 0 <= y < size_y:## return 0<= x<size_x and 0<=y<size_y
        return True
    else:
        return False


    
def print_map(size_x,size_y,pusher_x,pusher_y,boxes,dests):
    for y in range(size_y):
        for x in range(size_x):
       
            if (x == pusher_x and y == pusher_y):
                print(" P ",end='')
            elif check_overlap(y,x,boxes):
                print(" B ",end='')
            elif check_overlap(y,x,dests):
                print(" D ",end='')
            else:
                print(" - ",end='')
        print()

def input_process(direction):
    dx=0
    dy=0
    if direction == "W":
        dy -=1
            
    elif direction == "S":
        dy +=1

    elif direction == "A":
        dx -=1
    elif direction == "D" :        
        dx +=1
    else:
        print("you enter wrong button pls this agian bro:")
    return dx , dy

#main-----GAME_LOOP--------
while True:
    print_map(size_x,size_y,pusher_x,pusher_y,boxes,dests)

    direction = input("What is your next move?(W/A/S/D)").upper()
    #xu li dau vao
    dx,dy= input_process(direction)
    if  boxes == pusher_x + dx and boxes== pusher_y + dy:
        #truoc mat cua thang day hop
        
       
        for box in boxes:
                        
            if is_in_map(pusher_x+dx,pusher_y+dy,size_x,size_y):
                box["x"]=pusher_x+dx
                box["y"]=pusher_y+dy
                pusher_x += dx
                pusher_y += dy
            else:
                            
                print("you can't push")
                
    else:
        next_pusher_x =  pusher_x + dx
        next_pusher_y = pusher_y + dy
        if is_in_map(next_pusher_x, next_pusher_y,size_x,size_y):
            
            pusher_x += dx
            pusher_y += dy
        else:
            print("you can't go")

    if boxes == dests:
        
        break
print("u win")    








