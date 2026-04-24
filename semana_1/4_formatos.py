
import csv

datos = [
    ['Nombre', 'Edad', 'Ciudad'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 15, 'Chicago'],
    ['Carlos', 50, 'Chicago'],
    ['Edily', 33, 'Chicago'],
    ['Jose', 11, 'Chicago'],
]

#* Crear y Escribir en un archivo csv.
with open('personas.csv', 'w', newline='', encoding='utf-8') as archivo_csv:
    escrito = csv.writer(archivo_csv)
    escrito.writerows(datos) # Escribe todas las filas a la vez.
    print('Archivo CSV creado con éxito.')



#TODO: TAREA: Python puedes leer un archivo Excel (.xlsx, .xls) 
# y guardar su contenido como un archivo CSV. 
# Esto es muy útil para transformar datos de un formato binario a un formato de texto universal.

#TODO: TAREA: Crear un archivo Excel (.xlsx) → archivo binario.
# se escribe con librerías externas (no con open simple).
# Debes usar una librería externa como openpyxl (no se puede con with de la misma manera):

#TODO: TAREA: Crear un archivo Word, también requiere librerías como python-docx.