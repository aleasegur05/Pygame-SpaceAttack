import pygame

class Colores:
    #LOS COLORES
    BLANCO=(255,255,255)
    NEGRO=(0,0,0,0)
    ROJO=(255,0,0)
    AZUL=(0,0,255)
    VERDE=(0,255,0)

    def actualizar_elementos(VENTANA, color1,color2,color3,color4,color5):
        width, height = VENTANA.get_size()

    # EJE X | EJE Y | ANCHO X | ALTO Y
        puntosRectangulo=(width // 8, height // 12, width // 8, height // 12)
        rectangulo1 = pygame.draw.rect(VENTANA, color1, puntosRectangulo)

    # COMIENZO DE LA LINEA | INCLINA LA LINEA | FINAL DE LA LINEA | INCLINA LA LINEA | GROSOR
        puntosLinea1=(width // 8, height // 6)
        puntosLinea2=(width // 4, height // 6)
        linea1=pygame.draw.line(VENTANA, color2, puntosLinea1, puntosLinea2, 10)

    # X | Y | RADIO | VACIO
        puntosCirculo=(width // 6, height // 2)
        grosorCirculo=min(width, height) // 30
        circulo1=pygame.draw.circle(VENTANA,color3,puntosCirculo, grosorCirculo)

    # X | Y | TAMAÑO X | TAMAÑO Y | GRUESO (OPCIONAL)
        puntosElipse=(width // 3, height // 3, width // 20, height // 7)
        elipse1=pygame.draw.ellipse(VENTANA, color4, puntosElipse, 10)

        puntosPoligono=[(width // 8, height // 2), (width // 8, height // 6)]
        poligono1=pygame.draw.polygon(VENTANA, color5, puntosPoligono, 8)

