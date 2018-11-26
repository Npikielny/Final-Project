from ggame import App, Color, LineStyle, Sprite, CircleAsset, Frame, RectangleAsset
from math import floor, sin, cos, tan, log

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
    print("RGB string just before feeding it through GGame color", output)
    return (Color(output, alpha))

Outline = LineStyle(1,Color(0xFF0000,1.0))
print("Color using GGame color", Color(0x050505, 1.0))
print("Color using RGB conversion", color(5,5,5, 1.0))
rect = RectangleAsset(10,10,Outline,Color(0x050505,1.0))
Sprite(rect, (0,0))
#rect = RectangleAsset(10,10,Outline,Color(0x00C549,1.0))
#Sprite(rect, (0,0))
    
    
myapp = App()
myapp.run()
