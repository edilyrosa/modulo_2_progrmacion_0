
#* POO EN PY
# ┌──────────────────────┬─────────────────────────────────────────────────────┬────────────────────────────────────────────────┐
#*│      CONCEPTO        │                     DEFINICIÓN                      │             ANALOGÍA DEL MUNDO REAL            │
# ├──────────────────────┼─────────────────────────────────────────────────────┼────────────────────────────────────────────────┤
# │ Clase                │ Es la plantilla o molde. Define cómo será un  Obj   │ El plano de un arquitecto para una casa.       │
# │                      │                                                     │                                                │
# ├──────────────────────┼─────────────────────────────────────────────────────┼────────────────────────────────────────────────┤
# │ Objeto / Instancia   │ Es una copia real creada desde la clase.            │ Una casa específica construida con ese plano.  │
# ├──────────────────────┼─────────────────────────────────────────────────────┼────────────────────────────────────────────────┤
# │ Atributo             │ Son las características o datos que guarda un Obj   │ El color, metros cuadrados y pisos de la casa. │
# │                      │                                                     │ Variables que pertenecen al objeto             │
# ├──────────────────────┼─────────────────────────────────────────────────────┼────────────────────────────────────────────────┤
# │ Constructor          │ Método especial que se ejecuta al crear un Obj      │ El proceso de construir y equipar la casa.     │
# │                      │                                                     │                                                │
# ├──────────────────────┼─────────────────────────────────────────────────────┼────────────────────────────────────────────────┤
# │ Método               │ Son las acciones que puede realizar un objeto.      │ Abrir la puerta, encender las luces de la casa.│
# │                      │ Funciones que el objeto puede ejecutar              │                 (ej. encender, frenar).        │
# └──────────────────────┴─────────────────────────────────────────────────────┴────────────────────────────────────────────────┘

# Instanciar: El acto de crear un objeto específico a partir de la clase.
# Objeto: entidad que tiene "características" (atributos) y "habilidades" (métodos).

# * La Clase
# Se define con la palabra clave "class" seguida de un nombre en formato PascalCase 
# (primera letra de cada palabra en mayúscula). Por sí sola, la clase no hace nada; es solo el molde.

class Robot:
   pass
   # TODO: Desarrola esto
   # constructor(nombre, tarea) y ademas otro atr activo y sera bool, todos nacen activos
   # saludar()
   # apagar() → activos → false
   # estado() → me informa si etsa activo o no
   
   # crea algunas instancias