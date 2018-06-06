import math
def circle(r) :
    circle = r*math.pi*2
    print(circle)
def square(x,y) :
    square = x*y*2
    print(square)
def diamond(s) :
    diamond = s*4
    print(diamond)
def pentagone(s) :
    pentagone = s*5
    print(pentagone)
def hexagone(s) :
    hexagone = s*5
    print(hexagone)

while True:
    form = str(input('What object do you want the perimeter of : '))
    if (form == str('square')):
        x = float(input('Enter Length : '))
        y = float(input('Enter Width : '))
        square(x, y)
    elif (form == str('diamond')):
        s = float(input('Enter Side Length : '))
        diamond(s)
    elif (form == str('pentagone')):
        s = float(input('Enter Side Length : '))
        pentagone(s)
    elif (form == str('hexagone')):
        s = float(input('Enter Side Length : '))
        hexagone(s)
    elif (form == str('circle')):
        r = float(input('Enter Ray : '))
        circle(r)
    else :
        print("This form doesn't exist")
    restart = str(input('Do you want to calculate an other form perimeter : '))
    if restart == 'No' :
        break
