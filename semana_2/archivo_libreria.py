
# import math as m #*INTEGRADO EN EL INTERPRETE PY SOLO IMPORT
# import streamlit as st #*ESTA TENEMOS QUE INSTARLA CON PIP INSTALL + IMPORT
# print(m.pi)
# print(m.pow(2, 3))
# print(2**3)
# PI = 3.159

nombre = __name__
#! nombre = '__main__'
PI = 2.2
def saludar(nombre):
    print(f'Hola {nombre}')

if __name__ == "__main__": #*True: para que tus eje no se fueg a los archivos principales donde importes estas utilidades (consts, var, func)
    print(nombre) #__main__ #? orden de eje
    saludar('Edily')        #? orden de eje
    

# * __name__ 
# es una variable especial que representa el nombre del módulo actual. 
# Si el módulo se ejecuta directamente, __name__ será igual a "__main__". 
# Si el módulo se importa desde otro módulo, __name__ será igual al nombre del módulo. E.g: "mi_script"


#*💡 if __name__ == "__main__": 
# Ejecuta el código indentado solo cuando el script se ejecuta directamente, 
# no cuando se importa como módulo desde otro script.
# 
# → Asegura que la función main(), con conexión a Supabase y consulta, solo se ejecute cuando corras 
# ese archivo directamente. Si en el futuro importaras alguna función desde ese mismo archivo a otro programa, 
# no se dispararía automáticamente la consulta, evitando efectos secundarios no deseados.
#? if __name__ == "__main__":
    # main()