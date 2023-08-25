import pygame
import random

# Iniciar Pygame
pygame.init()


# Crear pantalla
pantalla = pygame.display.set_mode((800, 600))


# Titulo e Icono
pygame.display.set_caption("Invasion especial")
icono = pygame.image.load("tierra.png")
pygame.display.set_icon(icono)

fondo = pygame.image.load("fondo.gif")

# Jugador
img_jugador = pygame.image.load("nave.png")
jugador_x = 364
jugador_x_cambio = 0
jugador_y = 536
jugador_y_cambio = 50



# Enemigo
img_enemigo = pygame.image.load("aulab.png")
enemigo_x = random.randint(0, 736)
enemigo_x_cambio = 0.4
enemigo_y = random.randint(50, 200)
enemigo_y_cambio = 20


def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

def enemigo(x, y):
    pantalla.blit(img_enemigo, (x, y))


# Loop del juego
se_ejecuta = True
while se_ejecuta:
    # Primero se pinta la pantalla
    pantalla.fill((0, 0, 4))

    pantalla.blit(fondo, (0,0))

    # Eventos
    for e in pygame.event.get():
        # Evento cerrar
        if e.type == pygame.QUIT:
            se_ejecuta = False

        # Evento Presionar
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            if e.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3
            if e.key == pygame.K_UP:
                jugador_y_cambio = -0.3
            if e.key == pygame.K_DOWN:
                jugador_y_cambio = 0.3

        # Evento Soltar
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                jugador_x_cambio = 0
            if e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                jugador_y_cambio = 0

    # Coloca al jugador
    jugador_x += jugador_x_cambio

    jugador_y += jugador_y_cambio


    # Mantiene al jugador en sus bordes
    if jugador_x <= 0:
        jugador_x = 0

    elif jugador_x >= 736:
        jugador_x = 736
    
    if jugador_y <= 0:
        jugador_y = 0

    elif jugador_y >= 536:
        jugador_y = 536


    # Coloca al jugador
    enemigo_x += enemigo_x_cambio



    # Mantiene al enemigo en sus bordes
    if enemigo_x <= 0:
        enemigo_x_cambio = 0.4
        enemigo_y += enemigo_y_cambio

    elif enemigo_x >= 736:
        enemigo_x_cambio = -0.4
        enemigo_y += enemigo_y_cambio

    
   
        


    # Coloca a las entidades
    jugador(jugador_x, jugador_y)
    enemigo(enemigo_x, enemigo_y)

    pygame.display.update()
