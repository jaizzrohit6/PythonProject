#conditional

x = 4

#Basic if 
if x < 6: 
    print('This is true') #this is indent for loop
     
print("hi") #this another line out from loop due to indent

#if else
if x < 2:
    print('This is true')
else:
    print('This is false')    
    
#Elif

color = 'red'

if color == 'red':
    print('color is red')
elif color == 'blue':
    print('color is blue')
else:
    print('color is neither red nor blue')    

#nested if

if color == 'red':
    if x < 10:
        print('color is red and x less than 10')

#Logical Operator

if color == 'red' and x < 10:
    print('color  is red and x is less than 10')