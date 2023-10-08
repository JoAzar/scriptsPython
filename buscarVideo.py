amarillo = '\033[93m'
verde = '\033[92m'
rojo = '\033[91m'
subRayado = '\033[4m'
resetColor = '\033[0m'
texto="Buscar en YouTube: "
import webbrowser

busqueda = input(f"{amarillo}{subRayado}{texto}{resetColor}")
enlace_busqueda = f"https://www.youtube.com/results?search_query={busqueda}"
#BUSCAR
webbrowser.open(enlace_busqueda)
