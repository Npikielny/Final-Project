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
        pt = CircleAsset(5, noLine, color)
        Sprite(pt, position)
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
        return point.color(abs(sin(funcIndex*0.2)*255),abs(cos(funcIndex*1.31)*255),abs(cos(2*funcIndex)*sin(funcIndex*0.5)*255), 1.0)
#-----------------------------------------------------
class collectionViewCell(Sprite):
    cell = RectangleAsset(200,60, LineStyle(1, point.color(100,100,100,0.5)), point.color(200,200,200,0.5))
    def __init__(self, position):
        super().__init__(collectionViewCell.cell, position)
class collectionView(Sprite):
    view = RectangleAsset(240,frameHeight, noLine, black)
    addFuncButton = RectangleAsset(200, 50, noLine, white)
    def __init__(self, position):
        super().__init__(collectionView.view, position)
        for i in range(1,11):
            collectionViewCell((20, 10 + i * (60 + 10)))
        button = RectangleAsset(60,60,LineStyle(1, point.color(250,250,250,0.5)))
        plusV = RectangleAsset(10,50,LineStyle(1, point.color(250,250,250,0.5)), white)
        plusH = RectangleAsset(50,10,LineStyle(1, point.color(250,250,250,0.5)), white)
        Sprite(button,(20,10))
        Sprite(plusV,(50-5,15))
        Sprite(plusH,(25,35))
    def dropdown(state):
        Func = Sprite(RectangleAsset(10,10,noLine, black), (10,10))
        Func.visible = state
            
#-----------------------------------------------------
class Grapher(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        collectionView((0,0))
        Grapher.listenMouseEvent("click", self.mouseClick)
        self.dropping = False
    def X(x):
        return(x + 240)
    for i in range(0,40):
            point((X(i*10),0), point.colorRandom(i))
    def mouseClick(self, event):
        #Dropping down menu
        if event.x < 80 and event.x > 20 and event.y < 80 and event.y > 20 and self.dropping == False:
            self.dropping = not self.dropping
            collectionView.dropdown(self.dropping)
        elif event.x < 80 and event.x > 20 and event.y < 40 and event.y > 20 and self.dropping == True:
            print("func")
        elif event.x < 80 and event.x > 20 and event.y < 60 and event.y > 40 and self.dropping == True:
            print("param")
        elif event.x < 80 and event.x > 20 and event.y < 80 and event.y > 60 and self.dropping == True:    
            print("constant")
    #-----------------------------------------------------
myapp = Grapher(frameWidth, frameHeight)
myapp.run()