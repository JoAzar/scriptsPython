import os

rojo = '\033[91m'
verde = '\033[92m'
amarillo = '\033[93m'
resetColor = '\033[0m'

archivo = input(amarillo+"Ingrese el nombre del archivo.tar.gz: "+resetColor)
if os.path.isfile(archivo):
    os.system(f"tar -xzvf {archivo}")
else:
    print(rojo+"El archivo no existe"+resetColor)
