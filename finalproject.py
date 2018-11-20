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
def funcInterpreter(depVar, indepVar, equation,t):
    if equation.count("(") != equation.count(")") or equation.count("=") != 1:
        print("Invalid input given")
    else:
        newEquation = ""
        for i in equation:
            if i != " ":
                newEquation += i
        #print("Interpreting:", newEquation)
        if newEquation.find("=") != 1:
            print("Implementation of implicits needed")
        else:
             equationR = newEquation[newEquation.find("=")+1: len(newEquation)]
        #     print("equationR", equationR)
             if equationR.count(indepVar) > 0 or indepVar == "nil":
                  pluggableEquation = pluggerSetup(depVar, indepVar, equationR)
        #          print("pluggable:", pluggableEquation)
             else:
                  b = getOperandsAndTerms(equationR)
                  pluggableEquation = prenEliminator(b[0],b[1])
        points = []
        #for i in range(1,10):
        #    points.append((funcPlugger(depVar, indepVar, str(pluggableEquation), i)))
        points.append((funcPlugger(depVar, indepVar, str(pluggableEquation), t)))
        #points = "nil"    
        return(points)
        
def funcCombiner(equation):
    #print(equation)
    equationL = getOperandsAndTerms(equation[0:equation.find("=")])
    #print(equationL)
    equationR = getOperandsAndTerms(equation[equation.find("="):len(equation)-1])
    #print(equationR)
    equationLOperators=[]
    for i in equationL[1]:
        if i == "-":
            equationLOperators.append("+")
        elif i == "+":
            equationLOperators.append("-")
        else:
            equationLOperators.append(i)
    return(equationR[0] + equationL[0],equationR[1] + equationLOperators[:])
      
def funcCompiler(terms, operands):
    output = ""
    for i in range(0, len(terms)):
        output += terms[i]
        if i < len(terms) - 1:
            output += operands[i]
    return(output)

def prenEliminator(terms, operands):
    newTerms = []
    operators = []
    for z in terms:
        newTerms.append(z)
    for z in operands:
        operators.append(z)
    pp = 1 #Status of parenthesis being present
    g = 0 #Just a method to stop infinite loops if there is an error in my code
    
    while pp == 1 and g != 20:
        #print("while", newTerms, "g=", g)
        #print("pren:", newTerms)
        #print("pren:", operands)
        g += 1
        pcheck = ""
            
        for i in range(0,len(newTerms)):
            if str(newTerms[i]).isdigit() == False:
                #print("Non-int detected in prenElim")
                p = str(newTerms[i]).count("(")
                term = ""
                newTerm = ""
                outside = ""
                for k in range(len(newTerms[i])):
                    currentTerm = (newTerms[i])[k]
                    term += currentTerm
                    if currentTerm == "(":
                        #print("Hey we found an opening parenthesis!", newTerms, k)
                        outside += term[0:len(term)-1:]
                        #print("This is the outside:", outside)
                        if len(outside) > 0:
                            #print("The outside is longer than 0")
                            if outside[len(outside) - 1] == ")" or outside[len(outside) - 1].isdigit() == True or outside[len(outside) - 1] == "x" or outside[len(outside) - 1] == "y":
                                #print("We decided to add a multiplier")
                                outside += "*"
                        term = "("
                    elif currentTerm == ")" and term[0] == "(" and len(term[1:len(term)-1:]) > 0:
                        term = term[1:len(term)-1:]
                        newTerm = str(funcSolver(getOperandsAndTerms(term)[0],getOperandsAndTerms(term)[1]))
                        outside += "{0}"
                        term = ""
                        outside = outside.format(newTerm)
                    elif currentTerm == ")" and term[0] == "(" and len(term[1:len(term)-1:]) == 0:
                        print("There is an empty term; Substituting 0")
                        term = ""
                        outside += "0"
                if len(term) > 0 and len(outside) > 0:
                    if outside[len(outside) - 1].isdigit() == True and term[0].isdigit == True:
                        term = "*" + term
                    outside += term
                    #print("cash me", outside, term)
                else:
                    outside += term
                    
                newTerms[i] = str(outside)
                ##print("newTerms[i]", newTerms[i])
        for h in newTerms:
            pcheck += str(h)
        if pcheck.count("(") == 0:
            pp = 0
    
    if len(newTerms) > 1:
        #print("Int Solver", newTerms)
        newTerms = funcSolver(newTerms, operands)
    ##print("returning")
                #Solving Inner parenthetical Terms Like (4 + (3 + 2))
    #print(newTerms, g, "G", pp, ": PP", pcheck, pcheck.count("("))
    return(newTerms) 

def getOperandsAndTerms(equation):
    #initial Seperation
    terms = []
    term = ""
    operands = []
    p = 0
    op = 1
    for i in str(equation):
        if i != " " and i != "'"  and i != "[" and i != "]":
            if i == "(" or i == "{":
                p += 1
                if term != "" and term.count("(") == 0:
                    terms.append(term)
                    term = ""
                    op = 0
                if op == 0 and p == 1:
                    #print("OP == 0", term, terms, operands)
                    operands.append("*")
            elif i == ")" or i == "}":
                p -= 1
            if p == 0 and i != ")" and i != "}":
                if i == "+" or i == "*" or i == "/" or i == "^":
                    operands.append(i)
                    op = 1
                    if term != "":
                        terms.append(term)
                        term = ""
                elif i == "-":
                    if op == 1:
                        op = 2
                        term += i
                    elif op == 2:
                        op = 0
                        term = term[0:len(term)-1]
                    else:
                        #minusOperator
                        operands.append(i)
                        op = 1
                        if term != "":
                            terms.append(term)
                            term = ""
                elif i.isdigit() == True or i == ".":
                    term += i
                    op = 0
                elif i.isdigit() == False:
                    if term != "":
                        terms.append(term)
                        term = ""
                        op = 0
                    terms.append(i)
                if len(terms) > len(operands) + 1:
                    operands.append("*")
                    op = 1
            elif p == 0 and (i == ")" or i == "}"):
                term += i
                terms.append(term)
                term = ""
                op = 0
            else:
                term += i
    if term != "":
        terms.append(term)
    #print("GottenTerms", terms, "GottenOperands", operands, "from", equation)
    return((terms,operands))
    
def funcSolver(terms, operands):
    #print("funcSolverCalled")
    #print("terms:", terms)
    #print("operands:", operands)
    newTerms = terms
    final = 0
    holder = ""
    found = 0
    if len(operands) > 0:
        for i in range(0,len(operands)):
            i = i - found
            if operands[i] == "^":
                newTerms[i] = float(terms[i])**float(terms[i+1])
                del newTerms[i+1]
                del operands[i]
                found += 1
        #print("expo:", newTerms, operands)
        found = 0
        for i in range(0,len(operands)):
            #print(found, terms, newTerms, operands)
            i = i - found
            #print(i,len(terms),len(operands))
            #print(terms,operands)
            if operands[i] == "*":
                newTerms[i] = float(terms[i])*float(terms[i+1])
                del newTerms[i+1]
                del operands[i]
                found += 1
            elif operands[i] == "/":
                newTerms[i] = float(terms[i])/float(terms[i+1])
                del newTerms[i+1]
                del operands[i]
                found += 1
        #print("mult:", newTerms)
        for i in range(0,len(operands)):
            if operands[i] == "-":
                newTerms[i+1] = str((-1)*float(terms[i+1]))
        #print("sub:", newTerms)
        for i in newTerms:
            final += float(i)
    else:
        final = ""
        for i in terms:
            for k in i:
                if k.isdigit() == True or k == "." or k == "-":
                    final += str(k)
        final = float(final)
    #print("solved:", final)
    return(final)

def funcPlugger(depVar, indepVar, equation, t):
    if equation.find("=") != -1:
        equation = equation[equation.find("=")+1:len(equation)]
    a = getOperandsAndTerms(equation.format(t))
    b = prenEliminator(a[0],a[1])
    c = 0
    #print("Wubbo", equation.format(t),a,b)
    if isinstance(b, (list,)):
        #print(b)
        for i in b:
            c += float(i)
    else:
        c = b
    if depVar == "x":
        return(c,t)
    else:
        return(t,c)
        
def pluggerSetup(depVar, indepVar, equation):
    output = ""
    #print("PluggerSetup", depVar, indepVar, equation)
    for i in equation:
        #print("plug?", i, i == indepVar)
        if i == indepVar:
            if len(output)>0:
                if output[len(output)-1].isdigit():
                    output += "*"+"{0}"
                else:
                    output += "{0}"
            else:
                output += "{0}"
        elif len(output)>0: 
            if output[len(output)-1] == "}" and i.isdigit():
                output += "*"+i
            else:
                output += i
        else:
            output += i
        #print(output)
    return output

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
    return color(abs(255*sin(0.89*funcIndex+2.3)),abs(255*sin(0.44*funcIndex+1.5)),abs(255*sin(0.25*funcIndex+0.75)), 1.0)
#-----------------------------------------------------
class point(Sprite):
    pt = CircleAsset(5, outline, red)
    def __init__(self, position, color, equation, depVar):
        self.vy = 0
        self.vx = 0
        #print(funcInterpreter("y", "x", equation, 0.1))
        self.equation = equation
        self.depVar = depVar
        super().__init__(point.pt, position)

class drawnPoint(Sprite):
    def func(position, color):
        radius = 3
        pt = CircleAsset(radius, noLine, color)
        newPos = (position[0], position[1]-float(radius)/2.0)
        Sprite(pt, newPos)
    def deriv(position, color):
        radius = 3
        dr = CircleAsset(radius/2, LineStyle(1, color), white)
        newPos = (position[0], position[1]-float(radius)/2.0)
        Sprite(dr,newPos)
#-----------------------------------------------------
class Grapher(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        Grapher.listenMouseEvent("click", self.mouseClick)
        Grapher.listenKeyEvent("keydown","space", self.spacePressed)
        quadrant = RectangleAsset(float(frameWidth)/2-1, float(frameHeight)/2-1, outline, clear)
        grid = RectangleAsset(40,40, outline, white)
        for i in range(int(frameWidth/40)):
            for k in range(int(frameHeight/40)):
                Sprite(grid, (i*40,k*40))
                #print(i,k)
        self.going = False
        Sprite(quadrant, (0,0))
        Sprite(quadrant, (float(frameWidth)/2,0))
        Sprite(quadrant, (0,float(frameHeight)/2))
        Sprite(quadrant, (float(frameWidth)/2,float(frameHeight)/2))
        for i in range(20):
            drawnPoint.func((i*6 + 10,10), colorRandom(i))
    def mouseClick(self,event):
        if self.going == False:
            equation = input("Equation")
            indepVar = input("IndepVar")
            self.functions.append((equation, indepVar))
            try:
                b = funcInterpreter("y","x", equation, self.initial)[0]
            except:
                print("func failed")
                try:
                    b = funcInterpreter("y","x", equation, self.initial + self.increase / 2)[0]
                except:
                    print("Function Failed, Going to (0,0)", equation)
                    b = (0,0)
        point((getX(b[0]),getY(b[1])), colorRandom(len(self.functions)), equation, indepVar)
    def spacePressed(self,event):
        print(self.going)
        self.going = not self.going
    #-----------------------------------------------------
    initial = -1*float(frameWidth)/2 + 5.1
    #initial = 0
    increase = 1
    sproites = {}
    functions = []
    functions.append(("y=10", "y"))
    #functions.append(("y=20", "y"))
    #functions.append(("y=30", "y"))
    #functions.append(("y=40", "y"))
    #functions.append(("y=50", "y"))
    #functions.append(("y=60", "y"))
    #functions.append(("y=70", "y"))
    #functions.append(("y=80", "y"))
    #functions.append(("y=90", "y"))
    #functions.append(("y=100", "y"))
    #functions.append(("y=110", "y"))
    #functions.append(("y=120", "y"))
    #functions.append(("y=130", "y"))
    #functions.append(("y=140", "y"))
    #functions.append(("y=150", "y"))
    #functions.append(("y=160", "y"))
    #functions.append(("y=170", "y"))
    #drawnPoint((0,0),green)
    for i in range(0,len(functions)):
        try:
            b = funcInterpreter("y","x", functions[i][0], initial)[0]
        except:
            print("func failed")
            try:
                b = funcInterpreter("y","x", functions[i][0], initial + increase / 2)[0]
            except:
                print("Function Failed, Going to (0,0)", functions[i])
                b = (0,0)
        point((getX(b[0]),getY(b[1])), colorRandom(i), functions[i][0], functions[i][1])
        print("Graphing: ", functions[i])
        print(functions[i][0], functions[i][1])
    #drawnPoint.deriv((0,0),colorRandom(1))
    t = initial
    def step(self):
        g = self.increase
        if self.going == False:
            self.t = self.initial
        if self.going == True:
            self.t += g
            #print(self.t)
            funcNumber = 0
            for sprite in self.getSpritesbyClass(point):
                funcNumber += 1
                #print(self.sproites[sprite])
                #sprite.x += funcInterpreter("y","x","y=x",1)[0]
                indepVar = {"y":"x","x":"y"}
                try:
                    a = funcInterpreter(sprite.depVar,indepVar[sprite.depVar],sprite.equation,self.t)
                    b = funcInterpreter(sprite.depVar,indepVar[sprite.depVar],sprite.equation,self.t - g)
                except:
                    #print("Undefined value, shifting point.")
                    try:
                        a = funcInterpreter(sprite.depVar,indepVar[depVar],sprite.equation,self.t + g / 2)
                        b = funcInterpreter(sprite.depVar,indepVar[depVar],sprite.equation,self.t - 1 + g / 2)
                    except:
                        #print("Function Failed Twice, Going to (0,0)")
                        a = [(0,0)]
                        b = [(0,0)]
                #print("step", a, (a[0])[0])
                if isinstance(b, (list,)):
                    sprite.x = getX(((a[0])[0]))
                    sprite.y = getY(((a[0])[1]))
                    #print(getY(((a[0])[1])-((b[0])[1])))
                    #drawnPoint.deriv((getX(((a[0])[0])),getY(2*(((a[0])[1])-((b[0])[1])))), colorRandom(funcNumber))
                else:
                    sprite.x = getX(a[0])
                    sprite.y = getY(a[0])
                    print("Maybe something is off?")
                    #drawnPoint(getX(a[0]),getY(a[0]-b[0]))
                #print(a[1])
                #print(self.t, (sprite.x, sprite.y), sprite.equation)
                #print(sproites[sprite])
                #drawnPoint(sprite.x, sprite.y, colorRandom(funcNumber))
                drawnPoint.func((sprite.x,sprite.y),colorRandom(funcNumber))
                if sprite.depVar == "x":
                    if sprite.y > frameWidth or sprite.y < 0:
                        sprite.destroy()
                elif sprite.depVar == "y":
                    if sprite.x > frameHeight or sprite.x < 0:
                        sprite.destroy()
myapp = Grapher(frameWidth, frameHeight)
myapp.run()