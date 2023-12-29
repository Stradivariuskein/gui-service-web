import pystray
from PIL import Image
import os
import subprocess

# Cargar la imagen a utilizar como icono
image = Image.open('LOGO_LUQUE.png')

# Paso 4: Definir la función que se ejecutará al hacer clic en los elementos del menú
def on_clicked(icon, item):
    print('Hello World!')

# Paso 5: Definir la función para terminar la ejecución del icono
def on_quit(icon):
    icon.stop()

def run_server():
    # Directorio al que quieres moverte antes de ejecutar el comando
    target_directory = "../web-admin-luque"

    # Cambiar al directorio especificado
    os.chdir(target_directory)

    # Comando a ejecutar
    command = "python manage.py runserver"

    # Ejecutar el comando en un proceso separado
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, text=True)

    # Leer la salida del proceso línea por línea y mostrar en pantalla
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())  # Puedes modificar esto según tus necesidades

    # Esperar a que el proceso termine
    process.wait()

# Paso 6: Crear la instancia del icono y definir el menú
icon = pystray.Icon('Windows Menu', image, 'Windows Menu', menu=pystray.Menu(
    pystray.MenuItem('Run', run_server),
    pystray.MenuItem('Exit', on_quit),
))

# Paso 7: Ejecutar y mostrar el icono en la bandeja del sistema
icon.run()