import matplotlib.pyplot as plt

# Lista para almacenar los datos cargados desde el archivo
datos = []

# Lee el archivo de texto y procesa los datos
with open('sueldos.txt', 'r') as archivo:
    for linea in archivo:
        partes = linea.strip().split()
        if len(partes) == 3:
            empresa, fecha, sueldo = partes
            sueldo = float(sueldo.replace('.', '').replace(',', '.'))  # Reemplazar comas por puntos decimales y eliminar punto como separador de miles
            datos.append({"empresa": empresa, "fecha": fecha, "sueldo": sueldo})


# Extrae las fechas y sueldos en listas separadas
fechas = [dato["fecha"] for dato in datos]
sueldos = [dato["sueldo"] for dato in datos]

# Convierte las fechas en un formato legible (puedes ajustar esto según tus necesidades)
fechas_legibles = [f"{fecha.split('/')[0]}/{fecha.split('/')[1]}" for fecha in fechas]

# Crea el gráfico de líneas
plt.figure(figsize=(10, 6))
plt.plot(fechas_legibles, sueldos, marker='o', linestyle='-', color='b')
plt.title("Evolución del Sueldo a lo largo de los Meses y Años")
plt.xlabel("Fecha (Mes/Año)")
plt.ylabel("Sueldo ($)")
plt.grid(True)

# Rota las etiquetas del eje x para que sean legibles si tienes muchas fechas
plt.xticks(rotation=45)

# Muestra el gráfico en la consola
plt.tight_layout()
plt.show()
