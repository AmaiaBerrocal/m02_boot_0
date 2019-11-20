import pygame, sys
from pygame.locals import *

class Termometro():
    def __init__(self):
        self.custome = pygame.image.load("")#poner ruta hacia la imagen elegida en la planificación
    
class MainApp():
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))
        pygame.display.set_caption("Termómetro")
        self.__screen.fill((244, 236, 203))
        
        self.termometro = Termometro()

    def __on_close(self):
        pygame.quit()
        sys.exit()

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__on_close()
                    
            self.__screen.blit(self.termometro.custome, (50, 34)) #coordenadas elegidas en la planificación
            pygame.display.flip()
            

if __name__ == '__main__':
    pygame.init()
    app = MainApp()
    app.start()
            
