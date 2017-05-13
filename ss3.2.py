<<<<<<< HEAD
print("WELCOM TO OUR SHOP")

clothes = ["T-Shirt","Swearter","Jeans"]

print("new item: 'c', item: 'r', update new item:'u', delete item 'd'")

while True:
    action = input("what do youn want?")
    action = action.upper()

    if action == "C":
        print("new item :Jeans")

    elif action == "R":
        print("Item in shop")
        itemx = 1
        for clothe in clothes:

            print("{0}.{1}".format(itemx,clothe))
            itemx +=1
    elif action == "D":
        aa = int(input("Position:"))
        clothes.pop(aa)
        print("Item in shop")
        itemx = 1
        for clothe in clothes:

            print("{0}.{1}".format(itemx,clothe))
            itemx +=1
    elif action == "U":
        clothes.insert(1,"Skirt")
        
        
        
        
        
        
=======
print("WELCOM TO OUR SHOP")

clothes = ["T-Shirt","Swearter","Jeans"]

print("new item: 'c', item: 'r', update new item:'u', delete item 'd'")

while True:
    action = input("what do youn want?")
    action = action.upper()

    if action == "C":
        print("new item :Jeans")

    elif action == "R":
        print("Item in shop")
        itemx = 1
        for clothe in clothes:

            print("{0}.{1}".format(itemx,clothe))
            itemx +=1
    elif action == "D":
        aa = int(input("Position:"))
        clothes.pop(aa)
        print("Item in shop")
        itemx = 1
        for clothe in clothes:

            print("{0}.{1}".format(itemx,clothe))
            itemx +=1
    elif action == "U":
        clothes.insert(1,"Skirt")
        
        
        
        
        
        
>>>>>>> 81d5668b9368832001d3290f13dd8ad8a9cf6fe1
