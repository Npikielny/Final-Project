from ggame import App, Color, LineStyle, Sprite, CircleAsset, Frame, RectangleAsset
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
    def __init__(self, position, func):
        funcOut = int(str(func)*6)
        funcColor = Color(0x0 + funcOut, 1.0)
        pt = CircleAsset(5, noLine, funcColor)
        Sprite(pt, position)
    def color(red, green, blue):
        letters = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
        output = ""
        for i in (red, green, blue):
            if floor(i / 16) >= 10:
class Grapher(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        Sprite(RectangleAsset(width, height, noLine, white))
        for i in range(0,10):
            point((i*5, 0), i)
        point.color(1,2,3)

        

myapp = Grapher(frameWidth, frameHeight)
myapp.run()