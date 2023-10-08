
from PIL import Image
amarillo = '\033[93m'
reset_color = '\033[0m'
rojo = '\033[91m'
verde = '\033[92m'

def image_to_ascii(image_path, output_width, output_height):
    image = Image.open(image_path)
    image = image.resize((output_width, int(output_width * image.height / image.width)))
    ascii_chars = "@%#*+=-:. "
    ascii_image = ""

    for y in range(image.height):
        for x in range(image.width):
            pixel_color = image.getpixel((x, y))
            gray_value = int((pixel_color[0] + pixel_color[1] + pixel_color[2]) / 3)
            ascii_image += ascii_chars[gray_value * (len(ascii_chars) - 1) // 255]
        ascii_image += "\n"

    return ascii_image

if __name__ == "__main__":
    rutaImagen = input(amarillo+"Ingresa el nombre de la imágen ej: nido.png => "+reset_color)
    rutaImagenCompleta = "ruta/de/imagenes"+rutaImagen
    ascii_representation = image_to_ascii(rutaImagenCompleta, output_width=20, output_height=5)
    print(rojo+ascii_representation+reset_color)
