from ggame import App, Color, LineStyle, Sprite, CircleAsset, Frame, RectangleAsset
from math import floor, sin, cos
#-----------------------------------------------------
red = Color(0xff0000, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
green  = Color(0x0fff6f, 1.0)
white = Color(0xffffff, 1.0)
#-----------------------------------------------------
frameWidth = 800
frameHeight = 800
#-----------------------------------------------------
noLine  = LineStyle(0, black)
#-----------------------------------------------------
class point(Sprite):
    def __init__(self, position, color):
        #if color <= 10:
        #pt = CircleAsset(5, noLine, (color * sin(color)), color * cos(color), 1)
        #else:
        pt = CircleAsset(5, noLine, color)
        Sprite(pt, position)
    def color(red, green, blue):
        letters = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
        output = "0x"
        for i in (int(red), int(green), int(blue)):
            a = int(floor(i / 16))
            if a >= 10:
                output += str(letters[a])
            else:
                output += str(a)
            if i - a*16 >= 10:
                output += str(letters[i - a*16])
            else:
                output += str(i - a*16)
        return (Color(output, 1.0))
        
    def colorRandom(funcIndex):
        return point.color(abs(sin(funcIndex*0.2)*255),abs(cos(funcIndex*1.3)*255),abs(cos(2*funcIndex)*sin(funcIndex*0.5)*255))

class function():
    functions = {}
    def __init__(self, inputString):
        
    def funcType():
class Grapher(App):
    
    def __init__(self, width, height):
        super().__init__(width, height)
        Sprite(RectangleAsset(width, height, noLine, white))
        for i in range(0,40):
            point((i*10,0), point.colorRandom(i))
    def function(inputString):
        functionType = 0
        left = 0
        xPres = 0
        yPres = 0
        for i in inputString:
            if left != 1:
                if i == "=":
                    left = 1
                elif i == "x" and x == 0:
                    functionType += 1
                    x += 1
                elif i == "y" and y == 0:
                    functionType += 1
                    y += 1
        functions[len(functions)] = inputString
        functionsType[len(functions)] = functionType
myapp = Grapher(frameWidth, frameHeight)
myapp.run()