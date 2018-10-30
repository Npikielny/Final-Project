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
outline = LineStyle(1,black)
#-----------------------------------------------------
def prenEliminator(terms, operands):
    newTerms = []
    operators = []
    for z in terms:
        newTerms.append(z)
    for z in operands:
        operators.append(z)
    pp = 1
    g = 0
    ##print("size?",newTerms,operators)
    while pp == 1 and g != 5:
        ##print("while", newTerms)
        ##print("pren:", newTerms)
        ##print("pren:", operands)
        g += 1
        pcheck = ""
            
        for i in range(0,len(newTerms)):
            ##print("i", newTerms[i])
            if str(newTerms[i]).isdigit() == False:
                p = str(newTerms[i]).count("(")
                ##print("Implementation needed")
                term = ""
                newTerm = ""
                outside = ""
                for k in newTerms[i]:
                    ##print("k", k)
                    term += k
                    #print("length:", len(term[1:len(term)-1:]))
                    if k == "(":
                        outside += term[0:len(term)-1:]
                        if len(outside) > 0:
                            if outside[len(outside) - 1].isdigit() == True or outside[len(outside) - 1] == "x" or outside[len(outside) - 1] == "y":
                                outside += "*"
                        term = "("
                    elif k == ")" and term[0] == "(" and len(term[1:len(term)-1:]) > 0:
                        term = term[1:len(term)-1:]
                        ##print("calling newTerm", getOperandsAndTerms(term)[0],getOperandsAndTerms(term)[1])
                        #newTerm = str(funcSolver(getOperandsAndTerms(term))[0],getOperandsAndTerms(term)[1])
                        newTerm = str(funcSolver(getOperandsAndTerms(term)[0],getOperandsAndTerms(term)[1]))
                        outside += "{0}"
                        term = ""
                        outside = outside.format(newTerm)
                    elif k == ")" and term[0] == "(" and len(term[1:len(term)-1:]) == 0:
                        print("There is an empty term; Substituting 0")
                        term = ""
                        outside += "0"
                    ##print("term", term)
                ##print("final term", term)
                if len(term) > 0:
                    if term[0].isdigit() == True:
                        term = "*" + term
                    ##print("cash me", outside, term)
                    outside += term
                ##print(outside)
                newTerms[i] = str(outside)
                ##print("newTerms[i]", newTerms[i])
        for h in newTerms:
            pcheck += str(h)
        if pcheck.count("(") == 0:
            pp = 0
    
    if len(newTerms) > 1:
        ##print("final Solver")
        newTerms = funcSolver(newTerms, operands)
    ##print("returning")
                #Solving Inner parenthetical Terms Like (4 + (3 + 2))
    ##print(newTerms, g, "G", pp, ": PP", pcheck, pcheck.count("("))
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
            if i == "(":
                p += 1
            elif i == ")":
                p -= 1
            if p == 0 and i != ")":
                if i == "+" or i == "*" or i == "/" or i == "^":
                    operands.append(i)
                    op = 1
                    if term != "":
                        terms.append(term)
                        term = ""
                elif i == "-":
                    #Negative
                    if op == 1:
                        op = 2
                        term += i
                    else:
                        #minusOperator
                        operands.append(i)
                        op = 1
                        if term != "":
                            terms.append(term)
                            term = ""
                elif i.isdigit() == True or  i == ".":
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
            else:
                term += i
    if term != "":
        terms.append(term)
    ##print("GottenTerms", terms, "GottenOperands", operands, "from", equation)
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
            if operands[i] == "^":
                i = i - found
                newTerms[i] = float(terms[i])**float(terms[i+1])
                del newTerms[i+1]
                del operands[i]
                found += 1
        #print("expo:", newTerms, operands)
        found = 0
        for i in range(0,len(operands)):
            #print(i,len(terms),len(operands))
            #print(terms,operands)
            i = i - found
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
        ##print("sub:", newTerms)
        for i in newTerms:
            final += float(i)
    else:
        final = ""
        for i in terms:
            for k in i:
                if k.isdigit() == True or k == "." or k == "-":
                    final += str(k)
        final = float(final)
    ##print("solved", final)
    return(final)

def funcPlugger(depVar, indepVar, equations, funcNumb, t):
    substitueValues = list(range(-100,100))
    a = getOperandsAndTerms(i.format(t))
    b = funcSolver(a[0],a[1])
    if depVar == "x":
        print(b,k)
        point(coordinateTransfer((b,t*10)),colorRandom(funcNumb))
    else:
        print(k,b)
        point(coordinateTransfer((t,b*10)),colorRandom(funcNumb))

def coordinateTransfer(position):
    x = position[0]
    y = position[1]
    x = x + frameWidth / 2
    y = y*-1 + (frameHeight / 4) 
    return((x,y))
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
class point(Sprite):
    def __init__(self, position, color):
        pt = CircleAsset(5, outline, color)
        Sprite(pt, position)
        #self.y = position[1]
        #self.x = position[0]
class drawnPoint(Sprite):
    def __init__(self, position, color):
        pt = CircleAsset(3, noLine, color)
        Sprite(pt, position)
#-----------------------------------------------------
class Grapher(App):
    def __init__(self, width, height):
        super().__init__(width, height)
    def X(x):
        return(x + 240)
    for i in range(0,40):
            point((X(i*10),0), colorRandom(i))
    functions = []
    #functions.append("4+3*{0}+{0}-2/4")
    #functions.append("{0}^0.5")
    functions.append("1/{0}")
    for i in range(len(functions)):
        print(functions[i])
        b = []
        b.append(functions[i])
        #funcPlugger("y","x",b,i)
    #-----------------------------------------------------
    
    
    
    
    
    
    
    
myapp = Grapher(frameWidth, frameHeight)
myapp.run()