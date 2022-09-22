import turtle
import random
import time

class Circuito():
    corredores = [] #atributo de la clase
    __posStart = (-30, -10, 10, 30)
    __colorTurtle = ('red','blue','green','orange')

    def __init__(self, width, height): #inicio el constructor de Circuito
        self.__screen = turtle.Screen() #se declara la instancia de turtle como privada
        self.__screen.setup(width,height)
        self.__screen.bgcolor('lightgrey')
        self.__startLine = -width/2 + 20
        self.__finishLine = width/2 - 20

        self.__createRunners()

    def __createRunners(self):
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.shape('turtle')
            new_turtle.penup()
            new_turtle.setpos(self.__startLine, self.__posStart[i])# posiciono a las tortugas en sus lineas
            self.corredores.append(new_turtle)# meto new_turtle en el array corredores

    def competir(self):
        hayGanador = False
        while not hayGanador: # mientras no cambie el estado de hayGanador a True
            for tortuga in self.corredores: # se recorre la lista corredores
                avance = random.randint(1,6) # se genera un numero random 
                tortuga.forward(avance) # se le asigna el numero random a cada tortuga 

                if tortuga.position()[0] >= self.__finishLine: # si 
                    hayGanador = True
                    print("la tortuga de color {} ha ganado".format(tortuga.color()[0]))



if __name__ == '__main__': #si se ejecuta desde el programa principal main
    circuito = Circuito(640,480)
    circuito.competir()
    #time.sleep(5)
