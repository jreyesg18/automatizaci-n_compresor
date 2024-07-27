# automatizacion_compresor

# Image Compressor

Este proyecto es una herramienta en Python para comprimir imágenes en formatos `.jpg`, `.jpeg`, y `.png`. Utiliza la biblioteca `Pillow` para realizar la compresión de imágenes.

## Requisitos

- Python 3.x
- Pillow

## Instalación

1. **Clona el repositorio (si corresponde):**

   ```sh
   git clone <URL_DEL_REPOSITORIO>
   cd <DIRECTORIO_DEL_PROYECTO>
2. **Crea y activa un entorno virtual (opcional pero recomendado):**
    ```sh
    Copiar código
    python3 -m venv venv
    source venv/bin/activate
3. **Instala las dependencias:**
    ```sh
    Copiar código
    pip install Pillow
## Configuración

1. **Establece la ruta de la carpeta de descargas:**
Modifica el archivo main.py para establecer la ruta correcta a la carpeta donde están las imágenes que deseas comprimir. Cambia la variable downloadsFolder:

    ```python
    downloadsFolder = "/ruta/a/tu/carpeta/de/descargas/"
## Uso

1. **Ejecuta el script:**
Asegúrate de que tu entorno virtual esté activado (si lo estás usando) y ejecuta el script:

    ```sh
    python main.py
2. **Proceso:**
El script recorrerá los archivos en la carpeta especificada, comprimirá las imágenes en formato .jpg, .jpeg, y .png, y guardará las imágenes comprimidas con un prefijo compressed_.

## Ejemplo de salida

    ```sh
    
    Comprimido: imagen1.jpg
    Comprimido: imagen2.png
