d = {
    "apples" : 15,
    "bananas" : 35,
    "grapes" : 12
    }
print(d["bananas"])

d["oranges"] = 20

print(len(d))

"grapes" in d

d["pears"] = 19

d.get("pear", 0)

print(d)

fruits = list(d.keys())
fruits.sort()
print(fruits)
del d["apples"]
"apples" in d
print(d)
