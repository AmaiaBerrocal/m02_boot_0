import pygame, sys, random

class Runner():
    __customes = ('tortuga', 'elefante', 'perro', 'gato')
    
    def __init__(self, x = 0, y = 0):
        
        ixCustome = random.randint(0, 3)
       
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome]))
        self.custome = pygame.transform.scale(self.custome, (32, 32))
        self.position = [x, y]
        self.name = ""
        
    def avanzar(self):
        self.position[0] += random.randint(1, 6)
        
        
class Game():
    runners = []
    __posY = (160, 200, 240, 280)
    __names = ("MUERTE", "Peste", "Guerra", "Hambre")
    __startLine = -5
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("images/cesped.jpg")
        pygame.display.set_caption("Carrera de animales")
        
        for i in range(4):
            theRunner = Runner(self.__startLine, self.__posY[i])
            theRunner.name = self.__names[i]
            self.runners.append(theRunner)
        
    def close(self):
        pygame.quit()
        sys.exit()
   
    def competir(self):
        hayGanador = False
        while not hayGanador:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    hayGanador = True
                    
            for runner in self.runners:
                runner.avanzar()
                if runner.position[0] >= self.__finishLine:
                    print("{} ha ganado".format(runner.name))
                    hayGanador = True
            
            self.__screen.blit(self.__background, (0,0))
                       
            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)
        
            pygame.display.flip() 
            
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
        
if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.competir()
    
