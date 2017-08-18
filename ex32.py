the_count = [1,2,3,5,6]
fruits = ["apple","orange","pears","apricots"]
change = [1,"pennies",2,"dimes",3,"quaters"]

#this first kind of for-lop goes through a list
for n in the_count:
    print(f"this is the count: {n}")

for i in change:
    print(f"change: {i}")

# build list
elements = range(0,6)
"""
# use range function to do 0 to 5 count
for i in range(0,6):
    print(f"adding {i} to the list")
    elements.append(i)
"""
for i in elements:
    print(i)
