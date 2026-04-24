
#? pip install pandas matplotlib

import pandas as pd
import matplotlib.pyplot as plt

#*leemos para obtener la data del archivo csv.
df = pd.read_csv("personas.csv", encoding="utf-8")

#*analizamos la data
promedio_edad = df['Edad'].mean()
joven = df.loc[df['Edad'].idxmin()] #joven es dict... joven['Edad']
mayor = df.loc[df['Edad'].idxmax()] #joven es dict... joven['Edad']
conteo_ciudad = df['Ciudad'].value_counts()
# lista[:2:-1]

#*mostramos analiticas
print('Promedio de edad:', promedio_edad)
print(f'El mas joven es: {joven['Nombre']}, con {joven['Edad']} anios',)
print(f'El mas mayor es: {mayor['Nombre']}, con {mayor['Edad']} anios',)
print('Distribucion por ciudad:\n', conteo_ciudad)

#* graficos
#*Barras
conteo_ciudad.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Distribución de cantidad de personas por Ciudad')
plt.xlabel('Ciudad')
plt.ylabel('Cantidad de Personas')
plt.savefig('grafico_barras.png')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#*histograma
df['Edad'].plot(kind='hist', bins=5, color='green', edgecolor='black')
plt.title('Histograma de Edades')
plt.xlabel('Edades')
plt.savefig('grafico_hist.png')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#? df.loc[df["Edad"].idxmin()]
# df["Edad"]: Selecciona la columna (serie) llamada "Edad" del DataFrame df.
# .idxmin(): Retorna el primer índice de la fila donde se encuentra el valor mínimo de esa columna.
# Ejemplo: índices [0,1,2,3] de → [25,18,30,22] → df["Edad"].idxmin() devuelve 1 (porque el 18 está en la fila con índice 1).

#? df.loc[...]: 
# seleccionar filas (y opcionalmente columnas) por el nombre del índice.
# Sintaxis: df.loc[etiqueta_fila, etiqueta_columna(opcional)]

# ?df.loc[df["Edad"].idxmin()] → devuelve la etiqueta de la fila con la edad mínima.
# df.loc[ ... ] → selecciona toda la fila que tenga esa etiqueta.
# El resultado es una Serie (una fila del DataFrame) con todos los datos de la persona más joven