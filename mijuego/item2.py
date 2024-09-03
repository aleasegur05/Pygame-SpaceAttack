import pygame

class ItemB:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #self.vida=1
        self.ancho=70
        self.alto=70
        self.velocidad=5
        #self.color="red"
        self.rect=pygame.Rect(self.x,self.y,self.ancho,self.alto)
        self.imagen=pygame.image.load("media/item-veloc.png")
        self.imagen=pygame.transform.scale(self.imagen, (self.ancho,self.alto))

    def dibujar(self,VENTANA):
        #pygame.draw.rect(VENTANA,self.color,self.rect)
        self.rect=pygame.Rect(self.x,self.y,self.ancho,self.alto)
        VENTANA.blit(self.imagen, (self.x,self.y))

    def movimiento(self):
        self.y += self.velocidad