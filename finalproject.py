from ggame import App, Color, LineStyle, Sprite, CircleAsset, Frame, RectangleAsset
from math import floor
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
    def color(red, green, blue):
        letters = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
        output = "0x"
        for i in (red, green, blue):
            a = int(floor(i / 16))
            if a >= 10:
                output += str(letters[a])
            else:
                output += str(a)
            if i - a*16 >= 10:
                output += str(letters[i - a*16])
            else:
                output += str(i - a*16)
        return 0x000000 + int(output)
                
class Grapher(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        Sprite(RectangleAsset(width, height, noLine, white))
        for i in range(0,10):
            point((i*5, 0), point.color(69, 5, 255))
        point.color(255,25,100)
myapp = Grapher(frameWidth, frameHeight)
myapp.run()