import turtle

#Calcula as coordenadas e adiciona à lista points
#Adds the coordinates to the "points" list
def point(x,y):
    obj.forward(x*extension)
    obj.left(90)
    obj.forward(y*extension)
    points.append(obj.pos())
    home(obj,1)

#Returna o objeto ao seu ponto inicial. Se não esta calculando as coordenadas, a linha é marcada
#Move the object to his initial point. If not calculating coordinates, the turtle line will appear
def home(obj,isPoint):
        obj.up()
        obj.home()
        obj.goto(ObjectOrigin)
        if not isPoint:
            obj.down()

#Desenha os pontos de espaço extension
#Here, "obj" does the base of the graphic, using the unit "extension"
def CreateBase():
    for length in range(11):
        obj.left(90)
        obj.forward(length*extension)
        obj.stamp()
        obj.write(str(length))
        home(obj,False)
        obj.forward(length*extension)
        obj.stamp()
        obj.write(str(length))
        home(obj,False)

#A coordenada inicial do objeto
#The initial coordinate of the object
ObjectOrigin = (-100,-100)

#Lista para guardar as coordenadas
#The coordinates will be saved in this list
points = []

#Espaço entre pontos. Unidade de medida
#Unit of measure. Space between points
extension = 40






#Pede a função matemática ao usuário. Deve ser inserida utilizando as regras matemáticas de Python. Exemplo: 2*x-7. Somente "x" pode ser usado.
#Asks the user for the math function. Must be inserted with Python Math Rules. E.g. 2*x-7. Only "x" can be used.
fx =  input("Function: ")

#Tela onde os desenhos serão feitos
#Screen where the graphic will be constructed
window = turtle.Screen()
window.screensize(1000,1000)

#"draw" desenhará a função
#The "draw" object draws the graphic
draw = turtle.Turtle()
home(draw,0)
draw.hideturtle()
draw.speed(0)

#obj será usado para calcular as coordenadas e desenhar a base do gráfico
#The "obj" object calculates the coordinates. Also, draws a basic graphic structure
obj = turtle.Turtle()
home(obj,0)
obj.speed(0)

CreateBase()

#"obj" e "draw" param de marcar suas trajetórias na tela
#No more lines of "obj" or "draw" will be seen in the screen
obj.up()
draw.up()

#Chama "point" para calcular as coordenadas e move "draw" para elas
#Calls the "point" function to get the coordinates and, after that, moves "draw" to them
for x in range(-5,10):
    y = eval(fx)
    point(x,y)
    draw.goto(points[x+5])
    draw.down()

#Espera o usuário clicar para fechar a tela
#If the user click on the screen here, the program will finish the execution
window.exitonclick()
