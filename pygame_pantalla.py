import pygame
import pygame.mixer as mixer
pygame.init()

# Dimensiones de la pantalla
DIMENSIONES_PANTALLA = (1900,1000)

# Crear la ventana
PANTALLA = pygame.display.set_mode(DIMENSIONES_PANTALLA)
pygame.display.set_caption("Palabras en palabra")

icono = pygame.image.load("pelota.JPG")
pygame.display.set_icon(icono)



######################## sonido despues paso a funcion (llamarla)
mixer.init()
mixer.music.load(r"C:\Users\TT\Desktop\PARCIAL-2-PROGRAMACION.-1-CORPUS-COBOS\SONIDO AMBIENTE- PARTIDO SIN PUBLICO [8Gk-lP0JtjQ].mp3") ####aca pongo la ruta

###### manejo el volumen del audio #####
mixer.music.set_volume(0.6)

mixer.music.play()
#######################

# Color de fondo
PANTALLA.fill((34, 139, 35))  # Verde futbol

# Bandera pal bucle
bandera_pantalla = True

# El Bucle principal pa la pantalla
while bandera_pantalla:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            bandera_pantalla = False



    pygame.display.update()

pygame.quit()















