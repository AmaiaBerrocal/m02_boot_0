import turtle

class Circuito():
    corredores = []
    __posStartY = (-30, -10, 10, 30)
    __colorTurtle = ('red','blue', 'green', 'orange')
    
    def __init__(self, largo, ancho):
        self.__screen = turtle.Screen()
        self.__screen.setup(largo, ancho)
        self.__screen.bgcolor('lightgray')
        self.__startline = -largo/2 + 20
        self.__finishline = largo/2 - 20
        
        self.__createRunners()
        
    def __createRunners(self):
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.shape('turtle')
            new_turtle.penup()
            new_turtle.setpos(self.__startline, self.__posStartY[i])
            
            
            self.corredores.append(new_turtle)






if __name__ == '__main__':
    campo = Circuito(640, 480)
    