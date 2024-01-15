verde = '\033[92m'
reset = '\033[0M'

def escribirArchivo(archivo):
    ingreso = input("Ingrese lo que desea almacenar: ")
    agregarEspacio = input("¿Quiere agregar espacio?: ")
    if agregarEspacio == "no":
        archivo.write(ingreso+"\n")
        archivo.close()
    else:
        ingreso = ingreso + " "
        archivo.write(ingreso)
    print(ingreso)

def leerArchivo(archivo):
    with open(archivo, 'r') as archivo:
        lineas = archivo.readlines()
    for linea in lineas:
        print(verde+linea.strip()+reset)

terminar = "si"
archivo = open("archivoTexto.txt","a") 

while(terminar == "si"):
    escribirArchivo(archivo)
    terminar = input("¿Desea seguir escribiendo?: ")
    while terminar != "si" and terminar != "no":
        print("Responda si o no por favor")
        terminar = input("¿Desea seguir escribiendo?: ")

leerArchivo("archivoTexto.txt")
archivo.close()
