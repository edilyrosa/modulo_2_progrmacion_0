
#* 2. Manejo de archivos con open() y el manejador with...:
#* Modos de apertura
# "r"	Lectura (default)
# "w"	Escritura (sobreescribe)
# "a"	Append (añade al final)
# "x"	Creación exclusiva (error si existe)
# "b"	Modo binario (ej: "rb", "wb")
# "t"	Modo texto (default)
# "+"	Lectura y escritura (ej: "r+")

#* ¿Por qué usar with?
# Cierra automáticamente el archivo al salir del bloque.
# Previene fugas de recursos.
# Código más limpio y seguro.


#* Crear y Escribir en un archivo.
with open('ejemplo.txt', 'w', encoding='utf-8') as archivo:
    archivo.write('Hola mundo! \n')
    archivo.write('Linea 2 \n')
    archivo.write('Línea 3 \n')
    

#* READ en un archivo.
with open('ejemplo.txt', 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()
    print(contenido)
    
with open('ejemplo.txt', 'r', encoding='utf-8') as archivo:
    for linea in archivo:
        print(linea.strip()) # strip() para eliminar el salto de línea al imprimir cada línea.
    

#* 3. Manejo de excepciones (try-except)
# Los errores con archivos son comunes: archivo no existe, permisos, disco lleno, etc. 
# Usamos try para capturarlos.

#* Excepciones típicas
# FileNotFoundError – El archivo no existe.
# PermissionError – Sin permisos.
# IsADirectoryError – Se esperaba un archivo y es un directorio.
# OSError – Error genérico del sistema.

try:  
    with open('no_existe.py', 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
        print(contenido) #!FileNotFoundError: [Errno 2] No such file or directory: 'no_existe.py'
except FileNotFoundError:
    print('El archivo no existe, Creandolo..')      
    with open('no_existe.py', 'w', encoding='utf-8') as f:
        f.write('# Soy un comentario')  
except PermissionError:
    print('No tienes permisos para acceder a este archivo.')
except Exception as e:
    print('Ocurrió un error:', e)  
    
    
#! Borrar un archivo
# No puedes usar with para borrar archivos o directorios. with es un manejador de contexto 
# que se usa para abrir y cerrar recursos automáticamente (archivos, conexiones, etc.). 
# Para eliminar archivos y directorios se usan funciones del módulo os y shutil, que no se integran con with.
