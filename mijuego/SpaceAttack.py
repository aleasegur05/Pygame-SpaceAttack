import pygame

from personaje import Personaje
from enemigo import Enemigo
from disparar import Disparar
from enemigoB import EnemigoB
from item import Item
from item2 import ItemB
import random

pygame.init()

#Constantes
ANCHO=1000
ALTO=800
VENTANA=pygame.display.set_mode([ANCHO,ALTO])# pygame.RESIZABLE)#configuracion del tamaño de la pantalla, RESIZABLE significa redimensionar
TITULO=pygame.display.set_caption("Space_Attack")#ESTABLECE EL TITULO DE LA PANTALLA
RELOJ=pygame.time.Clock()
FPS=60
FUENTE=pygame.font.SysFont("Arial", 40)
FONDO=pygame.image.load("media/miFondo.jpeg").convert()

#Variables

salir=True#booleana para entrar en el bucle

tiempo_pasado=0
tiempo_enemigos=500

pj = Personaje(ANCHO/2,ALTO-100)

y=0

#Enemigo tipo A
enemigos=[]
#enemigos.append(Enemigo(ANCHO/2,100))

#Enemigo tipo B
enemigosB=[]
#enemigosB.append(EnemigoB(ANCHO/2,100))

#Item Disparo
itemA=[]
tiempos_itemA = []


#Item Velocidad
itemB=[]

vida=10
puntos=0

balas=[]
ultima_bala=0
tiempo_entre_bala=200
ultimo_item = pygame.time.get_ticks()



#Funcion para crear balas del juego
def crear_balas():
    global ultima_bala

    if pygame.time.get_ticks() - ultima_bala > tiempo_entre_bala:
        balas.append(Disparar(pj.rect.centerx, pj.rect.top - 20))
        ultima_bala = pygame.time.get_ticks()

# Funcion para utilizar teclas para jugar al juego
def gestion_teclas(teclas):
    #if teclas[pygame.K_w]:
    #    pj.y -= pj.velocidad
    #if teclas[pygame.K_s]:
    #    pj.y += pj.velocidad
    if teclas[pygame.K_a]:
        if pj.x >= 0:
            pj.x -= pj.velocidad
    if teclas[pygame.K_d]:
        if pj.x + pj.ancho <= ANCHO:
            pj.x += pj.velocidad
    if teclas[pygame.K_SPACE]:
        crear_balas()
    
#Bucle del juego

while salir and vida>0:
    
    tiempo_pasado += RELOJ.tick(FPS)
    if tiempo_pasado >= tiempo_enemigos:
        enemigos.append(Enemigo(random.randint(0,ANCHO),-100))
        if puntos>20: 
            enemigosB.append(EnemigoB(random.randint(0,ANCHO),-50))
        tiempo_pasado = 0
    
    tiempo_actual = pygame.time.get_ticks()
    if tiempo_actual - ultimo_item >= 5000:
        itemA.append(Item(random.randint(0, ANCHO), -100))
        itemB.append(ItemB(random.randint(0, ANCHO), -50))
        ultimo_item = tiempo_actual
        
    # Variables dentro del bucle(modifica acciones dentro del juego)
    eventos=pygame.event.get()#devuelve una lista con todos los eventos del juego

    teclas=pygame.key.get_pressed()

    texto_vida=FUENTE.render(f"VIDA: {vida}", True, "white")
    texto_puntos=FUENTE.render(f"PUNTOS: {puntos}", True, "white")

    gestion_teclas(teclas)

    #recoore todos los eventos del juego
    for evento in eventos:
        if evento.type==pygame.QUIT:# permite salir de la pantalla
            salir=False

        # maneja el evento de redimensionamiento de la VENTANA y ajusta el tamaño de la VENTANA a las nuevas dimensiones
        #elif evento.type==pygame.VIDEORESIZE:
        #    VENTANA=pygame.display.set_mode((evento.w, evento.h), pygame.RESIZABLE)

   # width, height = VENTANA.get_size()# Obtén las dimensiones actuales de la VENTANA

    # Muestra la ventana y jugador
    y_relativa = y % FONDO.get_rect().height
    VENTANA.blit(FONDO, (0, y_relativa - FONDO.get_rect().height))  # Asigno a la VENTANA un tipo de color
    if y_relativa < ALTO:
        VENTANA.blit(FONDO, (0, y_relativa))
    y += 1
    pj.dibujar(VENTANA)

    #Muestra enemigo A
    for enemigo in enemigos.copy():  # Crea una copia de la lista enemigos
        enemigo.dibujar(VENTANA)
        enemigo.movimiento()

        if pygame.Rect.colliderect(pj.rect,enemigo.rect):
            vida-=1
            print(f"Te quedan {vida} vidas")
            enemigos.remove(enemigo)  # Ahora puedes eliminar el objeto de la lista original

        if enemigo.y > ALTO:
            enemigos.remove(enemigo)

        for bala in balas:
            if pygame.Rect.colliderect(bala.rect,enemigo.rect):
                enemigo.vida-=1
                balas.remove(bala)

        if enemigo.vida <= 0:
            enemigos.remove(enemigo)
            puntos += 1

    #Muestra enemigo B
    for enemig in enemigosB.copy():  # Crea una copia de la lista enemigosB
        enemig.dibujar(VENTANA)
        enemig.movimiento()

        if pygame.Rect.colliderect(pj.rect,enemig.rect):
            vida-=1
            print(f"Te quedan {vida} vidas")
            enemigosB.remove(enemig)

        if enemig.y > ALTO:
            enemigosB.remove(enemig)

        for bala in balas:
            if pygame.Rect.colliderect(bala.rect,enemig.rect):
                enemig.vida -= 1
                balas.remove(bala)

        if enemig.vida <= 0:
            enemigosB.remove(enemig)
            puntos += 2

    # Muestra balas al disparar
    for bala in balas:
        bala.dibujar(VENTANA)
        bala.movimiento()

        if bala.y < 0:
            balas.remove(bala)
    
    # Muestra itemA
    for item in itemA.copy():
        item.dibujar(VENTANA)
        item.movimiento()

        if pygame.Rect.colliderect(item.rect, pj.rect):
            itemA.remove(item)
            tiempo_entre_bala /= 2
            tiempos_itemA.append(pygame.time.get_ticks())  # Almacena el tiempo en que se activó el efecto
        
        if item.y > ALTO:
            itemA.remove(item)

    # Muestra ItemB
    for items in itemB.copy():
        items.dibujar(VENTANA)
        items.movimiento()

        if pygame.Rect.colliderect(items.rect, pj.rect):
            itemB.remove(items)
            pj.velocidad *= 2
            tiempo_itemB = pygame.time.get_ticks()  # Almacena el tiempo en que se activó el efecto
        
        if items.y > ALTO:
            itemB.remove(items)
    
    # ItemB limitador de uso por tiempo
    if 'tiempo_itemB' in locals() and pygame.time.get_ticks() - tiempo_itemB >= 10000:
        pj.velocidad /= 2  # Revierte el efecto
        if 'tiempo_itemB' in locals():
            del tiempo_itemB  # Elimina la variable para que no se vuelva a ejecutar
    
    # IteamA limitador de tiempo
    for tiempo in tiempos_itemA[:]:
        if pygame.time.get_ticks() - tiempo >= 10000:
            tiempo_entre_bala *= 2  # Revierte el efecto
            tiempos_itemA.remove(tiempo)
    

    #Dibujar puntos y vida
    VENTANA.blit(texto_vida, (20,20))
    VENTANA.blit(texto_puntos, (20,60))
    
    pygame.display.update()#se actualiza la pantalla


