import pygame
import random
import math
from pygame import mixer
# Iniciar Pygame
pygame.init()


# Crear pantalla
pantalla = pygame.display.set_mode((800, 600))


# Titulo e Icono
pygame.display.set_caption("Invasion especial")
icono = pygame.image.load("tierra.png")
pygame.display.set_icon(icono)

# Fondo
cuadros = [pygame.image.load(f'Start{i + 1}.png') for i in range(5)]
indice_cuadro_actual = 0
retraso = 150 
contador = 0

# Agregar musica

mixer.music.load("musica_fondo.mp3")
mixer.music.set_volume(0.1)
mixer.music.play(-1)

# Jugador
img_jugador = pygame.image.load("nave.png")
jugador_x = 364
jugador_x_cambio = 0
jugador_y = 536
jugador_y_cambio = 50


# balas
balas = []
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_x_cambio = 0
bala_y = 536
bala_y_cambio = 1
bala_visible = False


# Enemigo
img_enemigo = [] 
enemigo_x = [] 
enemigo_x_cambio = [] 
enemigo_y = [] 
enemigo_y_cambio = [] 
cantidad_enemigos = 8

# Texto Puntaje
puntaje = 0
fuente = pygame.font.Font("Pixel NES.otf", 32)
texto_x = 10
texto_y = 10

# Texto Final
juego_terminado = False

def texto_final():
    texto_final_juego = fuente.render("Juego Terminado", True, (255, 255, 255))
    pantalla.blit(texto_final_juego, (60, 200))


# funcion enseñar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("aulab.png"))
    enemigo_x.append(random.randint(0, 736)) 
    enemigo_x_cambio.append(0.4) 
    enemigo_y.append(random.randint(50, 200)) 
    enemigo_y_cambio.append(20) 

def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

def enemigo(x, y, enemigo):
    pantalla.blit(img_enemigo[enemigo], (x, y))

def disparar(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))
    
def colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt( math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2) )
    if distancia < 64:
        return True
    else: False


# Loop del juego
se_ejecuta = True
while se_ejecuta:
    # Primero se pinta la pantalla
    pantalla.fill((0, 0, 4))

    pantalla.blit(cuadros[indice_cuadro_actual], (0, 0))

    contador += 1
    if contador >= retraso:
        contador = 0
        indice_cuadro_actual += 1
        if indice_cuadro_actual >= len(cuadros):
            indice_cuadro_actual = 0

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
            if e.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound("disparo.mp3")
                sonido_bala.set_volume(0.3)
                sonido_bala.play()
                nueva_bala = {
                "x": jugador_x,
                "y": jugador_y,
                "velocidad": -5
                }
                balas.append(nueva_bala)
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


    # Modificar la posicion de los enemigos
    for e in range(cantidad_enemigos):

        hay_colision_jugador = colision(enemigo_x[e], enemigo_y[e], jugador_x, jugador_y)
        if hay_colision_jugador:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            juego_terminado = True
            break


        enemigo_x[e] += enemigo_x_cambio[e]

        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.4
            enemigo_y[e] += enemigo_y_cambio[e]

        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.4
            enemigo_y[e] += enemigo_y_cambio[e]

    # colision
        for bala in balas:
            colision_bala_enemigo = colision(enemigo_x[e], enemigo_y[e], bala["x"], bala["y"])
            if colision_bala_enemigo:
                sonido_colision = mixer.Sound("Golpe.mp3")
                sonido_colision.set_volume(0.4)
                sonido_colision.play()
                balas.remove(bala)
                puntaje += 1
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(20, 200)
                break
 
        enemigo(enemigo_x[e], enemigo_y[e], e)



    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    # Movimiento bala
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)
    
    


    # Coloca a las entidades
    jugador(jugador_x, jugador_y)
    mostrar_puntaje(texto_x, texto_y)
    if juego_terminado:
        texto_final()


    pygame.display.update()
