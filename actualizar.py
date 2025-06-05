import pygame
import os
import subprocess
import time

def reproducir_sonido(ruta_sonido):
    pygame.init()
    pygame.mixer.init()

    try:
        sonido = pygame.mixer.Sound(ruta_sonido)
        sonido.play()
        pygame.time.wait(int(sonido.get_length() * 1000))
    except pygame.error as e:
        print("Error al reproducir el sonido:", e)
    finally:
        pygame.quit()

def ejecutar_comando_terminal(comando):
    try:
        subprocess.run(comando, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Error al ejecutar el comando:", e)

if __name__ == "__main__":
    ruta_sonido = "ruta_al_archivo_de_sonido/sonido.mp3"
    if os.path.exists(ruta_sonido):
        ejecutar_comando_terminal("apt update && apt upgrade")
        time.sleep(3)
        reproducir_sonido(ruta_sonido)
