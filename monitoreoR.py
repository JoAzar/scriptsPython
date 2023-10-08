import psutil
import threading
import os
import keyboard
amarillo = '\033[93m'
resetColor = '\033[0m'
rojo = '\033[91m'
verde = '\033[92m'

def monitorearCpu():
    while not salir.is_set():
        perc_cpu = psutil.cpu_percent(interval=1, percpu=True)
        mem_virt = int(psutil.virtual_memory().used / (1024 ** 2))
        avail_mem = int(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)

        os.system('clear' if os.name=='posix'else'cls')
        estado = "[ Estado actual del PC ]"
        print(verde+f"{estado}\n"+resetColor+
	amarillo+f"CPU: "+resetColor+rojo+f"[ -=R=-[ {perc_cpu}% ]-=R=- ]\n"+resetColor+
	amarillo+f"Usando: "+resetColor+rojo+f"( {mem_virt} ) =>"+resetColor+amarillo+f"[ Mb de memoria ]\n"+resetColor+
	amarillo+f"Queda: "+resetColor+rojo+f"( {avail_mem}% ) =>"+resetColor+amarillo+f"[ memoria libre ]"+resetColor)

#para salir del ciclo
salir = threading.Event()

if __name__ == '__main__':
    try:
        monitor_thread = threading.Thread(target=monitorearCpu)
        monitor_thread.start()
        keyboard.wait('q')
    except KeyboadInterrupt:
        pass
    salida.flag.set()
    monitor_thread.join()
    print("saliendo...")
