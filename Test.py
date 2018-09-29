from ggame import App, Color, LineStyle, Sprite, CircleAsset, Frame, RectangleAsset
red = Color(0xff0000, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
green  = Color(0x0fff6f, 1.0)
white = Color(0xffffff, 1.0)
#-----------------------------------------------------
frameWidth = 800
frameHeight = 800
#-----------------------------------------------------
#-----------------------------------------------------
noLine  = LineStyle(0, black)

class spriteType(Sprite):
    def __init__(self,x,y):
        print(x,y)

class Game(App):
    a = 4
    def __init__(self, width, height):
        super().__init__(width, height)
        super().spriteType(a,a)

myapp = Game(frameWidth, frameHeight)
myapp.run()