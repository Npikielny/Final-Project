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
    print("Final String: ", output)
    #print(int(output))
    return (Color(int(output), alpha))

print(Color(0x050505, 0.1))
print(color(5,5,5,0.1))
#print(type(0x000000))
#print(Color(int("0x050505"),0.1))
#print(int("0x050505"))
#print(Color(550505-500000, 0.1))

