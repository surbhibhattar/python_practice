'''
1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
area = (1/2)*base*height
2. Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
rectangle area=length*width
If no shape is supplied then it should take triangle as a default shape

3. Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
*
**
***
if input is 4 then it should print

*
**
***
****
Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)

'''


def calculate_area(base, height, shape='triangle'):
    if(shape == "rectangle"):
        return base*height
    else:
        return (0.5)*base*height

# print(calculate_area(2,6,'rectangle'))

def print_pattern(lines):
    for i in range(1,lines+1):
        for j in range(1,i+1):
            print('*',end='')
        print('')

print_pattern(6)



