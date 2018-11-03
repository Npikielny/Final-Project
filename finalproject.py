from ggame import App, Color, LineStyle, Sprite, CircleAsset, Frame, RectangleAsset
from math import floor, sin, cos

#-----------------------------------------------------
red = Color(0xff0000, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
green  = Color(0x0fff6f, 1.0)
white = Color(0xffffff, 1.0)
clear = Color(0xffffff, 0.0)
#-----------------------------------------------------
frameWidth = 800
frameHeight = 800
#-----------------------------------------------------
noLine  = LineStyle(0, black)
outline = LineStyle(1,black) 
#-----------------------------------------------------
def color(red, green, blue, alpha):
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
    return (Color(output, alpha))
def colorRandom(funcIndex):
    return color(abs(sin(funcIndex*0.2)*255),abs(cos(funcIndex*1.31)*255),abs(cos(2*funcIndex)*sin(funcIndex*0.5)*255), 1.0)    
#-----------------------------------------------------
def getX(xValue):
    x = xValue + float(frameWidth) / 2.0 - 3
    return(x)
    
def getY(yValue):
    y = float(frameHeight) / 2.0 - yValue
    return(y)

def giveX(xValue):
    x = xValue - float(frameWidth) / 2.0 + 3
    return(x)
    
def giveY(yValue):
    y = (-1 * yValue + float(frameHeight) / 2.0)
    return(y)
#-----------------------------------------------------
class point(Sprite):
    pt = CircleAsset(5, outline, red)
    def __init__(self, position, color, equation):
        self.vy = 0
        self.vx = 0
        self.vy = 0
        self.vx = 0
        super().__init__(point.pt, position)


class drawnPoint(Sprite):
    def __init__(self, position, color):
        pt = CircleAsset(3, noLine, color)
        newPos = (position[0], position[1]-1.5)
        Sprite(pt, newPos)
#-----------------------------------------------------
class Grapher(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        Grapher.listenMouseEvent("click", self.mouseClick)
        for i in range(20):
            drawnPoint((i*6 + 10,0), colorRandom(i))
        quadrant = RectangleAsset(float(frameWidth)/2-1, float(frameHeight)/2-1, outline, clear)
        grid = RectangleAsset(40,40, outline, white)
        for i in range(int(frameWidth/40)):
            for k in range(int(frameHeight/40)):
                Sprite(grid, (i*40,k*40))
                #print(i,k)
        Sprite(quadrant, (0,0))
        Sprite(quadrant, (float(frameWidth)/2,0))
        Sprite(quadrant, (0,float(frameHeight)/2))
        Sprite(quadrant, (float(frameWidth)/2,float(frameHeight)/2))
                
    def mouseClick(self,event):
        print("click")
    #-----------------------------------------------------
myapp = Grapher(frameWidth, frameHeight)
myapp.run()