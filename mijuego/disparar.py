import pygame

class Disparar:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho=35
        self.alto=35
        self.velocidad=10
        self.color="white"
        self.rect=pygame.Rect(self.x,self.y,self.ancho,self.alto)
        self.imagen=pygame.image.load("media/plasma.png")
        self.imagen=pygame.transform.scale(self.imagen, (self.ancho,self.alto))

    def dibujar(self,VENTANA):
        #pygame.draw.rect(VENTANA,self.color,self.rect)
        self.rect=pygame.Rect(self.x,self.y,self.ancho,self.alto)
        VENTANA.blit(self.imagen, (self.x,self.y))

    def movimiento(self):
        self.y -= self.velocidad