import pygame.mixer as mixer 

########## COMO MANEJO EL SONIDO ############

def iniciar_sonido():
    mixer.init()
    mixer.music.load(r"C:\Users\TT\Desktop\PARCIAL-2-PROGRAMACION.-1-CORPUS-COBOS\SONIDO AMBIENTE- PARTIDO SIN PUBLICO [8Gk-lP0JtjQ].mp3") ####aca pongo la ruta

    ###### manejo el volumen del audio #####
    mixer.music.set_volume(0.5)

    mixer.music.play()


