import psutil
import threading
import os
import time

# Definir colores
amarillo = '\033[93m'
resetColor = '\033[0m'
rojo = '\033[91m'
verde = '\033[92m'
azul = '\033[94m'

def monitorearCpu():
    while not salir.is_set():
        perc_cpu = psutil.cpu_percent(interval=1, percpu=True)
        mem_virt = int(psutil.virtual_memory().used / (1024 ** 2))  # Convertir a MB
        avail_mem = int(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)  # % de memoria libre

        # Limpiar pantalla
        os.system('clear' if os.name == 'posix' else 'cls')

        # Mostrar datos con formato
        print(verde + "+======================================+" + resetColor)
        print(verde + "| Monitor de Uso de CPU y Memoria      |" + resetColor)
        print(verde + "+======================================+" + resetColor)
        
        print(amarillo + f"Estado actual del PC: " + resetColor)
        print(f"{azul}CPU Utilizada: {rojo}[ {perc_cpu}% ]{resetColor}")
        print(f"{amarillo}Memoria Usada: {rojo}[ {mem_virt} MB ]{resetColor}")
        print(f"{amarillo}Memoria Libre: {rojo}[ {avail_mem}% ]{resetColor}")
        print(amarillo + "--------------------------------------" + resetColor)
        print(amarillo + "Presiona 'q' y Enter para salir..." + resetColor)

# Evento de salida
salir = threading.Event()

if __name__ == '__main__':
    try:
        # Crear hilo para monitorear
        monitor_thread = threading.Thread(target=monitorearCpu)
        monitor_thread.start()

        # Esperar a que se presione 'q' para salir usando input()
        while True:
            if input() == 'q':
                break
    except KeyboardInterrupt:
        pass
    finally:
        salir.set()  # Salir del ciclo de monitoreo
        monitor_thread.join()  # Esperar que el hilo termine
        print(verde + "\nSaliendo... Gracias por usar el monitor." + resetColor)
