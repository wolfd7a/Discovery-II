import math
def circle(r) :
    circle = r*math.pi*2
    print(circle)
def square(x,y) :
    square = x*y*2
    print(square)
form = str(input('What object do you want the perimeter of : '))
if (form == str('square')):
    x = complex(input('Enter Length : '))
    y = complex(input('Enter Width : '))
    square (x,y)
else :
    r = complex(input('Enter Ray : '))
    circle(2)
