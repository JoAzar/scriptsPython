import subprocess
import getpass
import time
rojo = '\033[91m'
verde = '\033[92m'
amarillo = '\033[93m'
resetColor = '\033[0m'

print(verde+"+======================================+"+resetColor)
print(verde+"| Script de Actualización del Sistema  |"+resetColor)
print(verde+"+======================================+"+resetColor)
print(amarillo+"Actualizando, aguarde un momento..."+resetColor)
comandos = "apt update && apt full-upgrade"
resultado = subprocess.Popen(comandos, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
cont = 0
while resultado.poll() is None:
    if cont<=2:
        print(rojo+"|▇|"+resetColor, end="", flush=True)
        cont+=1
    elif 2 < cont <= 5:
        print(amarillo+"|▇|"+resetColor, end="", flush=True)
        cont+=1
    else:
        print(verde+"|▇|"+resetColor, end="", flush=True)
        cont+=1
    time.sleep(1)

print(amarillo+"[ Actualización finalizada con éxito ]"+resetColor+"\n")
