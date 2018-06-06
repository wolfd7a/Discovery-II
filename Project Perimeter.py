import math
# Import math to get pi exact value
def circle(r) :
    circle = r*math.pi*2
    print(circle)
#V0.1 define circle perimeter calculus
def square(x,y) :
    square = x*y*2
    print(square)
#V0.1 define square perimeter calculus
def diamond(s) :
    diamond = s*4
    print(diamond)
#V0.2 define diamond perimeter calculus
def pentagone(s) :
    pentagone = s*5
    print(pentagone)
#V0.2 define pentagone perimeter calculus
def hexagone(s) :
    hexagone = s*5
    print(hexagone)
#V0.2 define hexagone perimeter calculus

while True:
    form = str(input('What object do you want the perimeter of : '))
#User invite for form input
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
#V0.2 break to restart program on user input
