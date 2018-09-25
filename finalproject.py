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
class collectionViewCell(Sprite):
    cell = RectangleAsset(200,50, LineStyle(1, point.color(100,100,100,0.5)), point.color(200,200,200,0.5))
    def __init__(self, position):
        super().__init__(collectionViewCell.cell, position)
class collectionView(Sprite):
    cells = []
    view = RectangleAsset(240,frameHeight, noLine, black)
    def __init__(self, position):
        super().__init__(collectionView.view, position)
        for i in cells:
            print("yay")
        #    collectionViewCell((20, 10 + i * (50 + 10)))
class function():
    functions = {}
    def __init__(self, inputString):
        print("yay")
    def funcType():
        print("yay")
class Grapher(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        #Sprite(RectangleAsset(width, height, noLine, white), (0,0))
        for i in range(0,40):
            point((i*10,0), point.colorRandom(i))
        #collectionViewCell((20,10))
        for i in range(0,4):
            collectionView.cells.append(i)
        collectionView((0,0))
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
        functionsType[len(functions)] = functionTyp
myapp = Grapher(frameWidth, frameHeight)
myapp.run()