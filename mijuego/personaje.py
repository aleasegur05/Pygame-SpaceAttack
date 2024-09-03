import pygame

class Personaje:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vida=1
        self.ancho=125
        self.alto=125
        self.velocidad=10
        #self.color="green"
        self.rect=pygame.Rect(self.x,self.y,self.ancho,self.alto)
        self.imagen=pygame.image.load("media/nave_Pj.png")
        self.imagen=pygame.transform.scale(self.imagen, (self.ancho,self.alto))

    def dibujar(self,VENTANA):
        # pygame.draw.rect(VENTANA,self.color,self.rect)
        self.rect=pygame.Rect(self.x,self.y,self.ancho,self.alto)
        VENTANA.blit(self.imagen, (self.x,self.y))
