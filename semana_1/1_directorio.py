
# * Objetivos de la clase
# Comprender cómo interactuar con el sistema de archivos desde Python.
# Aprender a leer, escribir, crear y eliminar archivos y directorios.
# Utilizar el manejador de contexto with para operaciones seguras.
# Manejar errores comunes con try-except.

#* 1. El módulo os – Interfaz con el sistema operativo
# Permite ejecutar comandos del SO, manipular rutas, directorios y archivos.

import os

#* os.getcwd() → Retorna Directorio actual: carpeta desde donde se ejecutó el programa.
print( 'Estoy ejecutando en: ', os.getcwd()) 
# 1 Estoy ejecutando en:  C:\Users\edily\Desktop\modulo_2
# 2 Estoy ejecutando en:  C:\Users\edily\Desktop\modulo_2\semana_1



# *Ruta absolutia del del DIRECTORIO que estoy eje
print('Directorio', os.path.dirname(os.path.abspath(__file__))) 
# Directorio c:\Users\edily\Desktop\modulo_2\semana_1

# *Ruta absolutia del del ARCHIVO que estoy eje
print(__file__)                  # c:\Users\edily\Desktop\modulo_2\semana_1\1_directorio.py
print(os.path.abspath(__file__)) # ✅ c:\Users\edily\Desktop\modulo_2\semana_1\1_directorio.py


# *Nomre del ARCHIVO que estoy eje
print(os.path.basename(os.path.abspath(__file__))) # 1_directorio.py


#* Crear una carpeta
# Crea una carpeta llamada nueva_carpeta en el directorio actual
#os.mkdir('nueva_carpeta')     #!FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'nueva_carpeta'
#os.mkdir('test/nueva_carpeta_1') #!FileNotFoundError: [WinError 3] The system cannot find the path specified: 'test/nueva_carpeta'


#* Crear una ruta se forma segura
ruta_segura = os.path.join(os.getcwd(), 'subcarpeta') #C:\Users\edily\Desktop\modulo_2\semana_1\subcarpeta
print('r', ruta_segura) 
# r C:\Users\edily\Desktop\modulo_2\semana_1\test\subcarpeta
# r C:\Users\edily\Desktop\modulo_2\semana_1\subcarpeta

#* crear acrpetas y evitar el error  #!FileExistsError
os.makedirs(ruta_segura, exist_ok=True) #*✅

#*ver el contenido de un directorio
contenido = os.listdir('.')
print(contenido) #['1_directorio.py', 'nueva_carpeta', 'subcarpeta', 'test']