from PIL import Image
import os

# Ruta a la carpeta de descargas (asegúrate de que esta ruta sea correcta)
downloadsFolder = "/ruta/a/tu/carpeta/de/descargas/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(filename)

        if extension.lower() in [".jpg", ".jpeg", ".png"]:
            try:
                # Construye la ruta completa al archivo
                filepath = os.path.join(downloadsFolder, filename)

                # Abre la imagen
                picture = Image.open(filepath)

                # Construye la ruta para el archivo comprimido
                compressed_filepath = os.path.join(downloadsFolder, "compressed_" + filename)

                # Guarda la imagen comprimida
                picture.save(compressed_filepath, optimize=True, quality=60)

                print(f"Comprimido: {filename}")
            except Exception as e:
                print(f"No se pudo procesar {filename}. Error: {e}")
