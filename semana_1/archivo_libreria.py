

#* __name__ 
# es una variable especial que representa el nombre del módulo actual. 
# Si el módulo se ejecuta directamente, __name__ será igual a "__main__". 
# Si el módulo se importa desde otro módulo, __name__ será igual al nombre del módulo.

    
# Cuando a script is run directly, __name__ is set to "__main__".
# Cuando imported, __name__ is set to the module's name. E.g: "mi_script"

#💡 if __name__ == "__main__": 
# Ejecuta el código indentado solo cuando el script se ejecuta directamente, 
# no cuando se importa como módulo desde otro script.
# 
# → Asegura que la función main(), con conexión a Supabase y consulta, solo se ejecute cuando corras 
# ese archivo directamente. Si en el futuro importaras alguna función desde ese mismo archivo a otro programa, 
# no se dispararía automáticamente la consulta, evitando efectos secundarios no deseados.
#? if __name__ == "__main__":
    # main()