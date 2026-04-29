# 
#* Programación Orientada a Objetos (POO)
# Es un paradigma de programación que organiza el código en objetos 
# que contienen datos (atributos) y comportamiento (métodos). 
# Se basa en clases (planillas o moldes) y objetos (instancias de esas clases).

#* Ventajas:
# Reutilización de código.
# Organización más clara.
# Modela mejor el mundo real.

#* Clases y objetos
# Clase: Plantilla que define atributos y métodos comunes a un tipo de objeto (abstracción).
# Objeto: Ejemplar concreto de una clase. Cada objeto tiene sus propios valores para los atributos.

#* Atributos (son variables)
# Atributos de clase: Son compartidos por todos los objetos de la clase. Se definen fuera de cualquier método.
# Atributos de instancia: Pertenecen a cada objeto por separado. Se crean con self dentro de métodos.
# TODO: Investigar los atributos privados (con __) y protegidos (con _) y su convención de uso.
# TODO: Investigar los getters y setters, y la función property para control de acceso a atributos.
class Perro: #la clase misma sera la constructora
        especie = 'Can familiaris' # Atributos de clase
        def __init__(self, nombre, edad): #todos los metodos de instancia requieren como 1er parametro "self"
                self.nombre = nombre #Atributos de instancia
                self.edad = edad
        #* El método __init__ y self
        # El método __init__ es el constructor. 
        # Se ejecuta automáticamente al crear un objeto.
        # El parámetro self hace referencia al objeto que se está creando. 
        # Por convención se llama self, pero podría tener otro nombre (aunque no se recomienda).
        
        def ladrar(self):
                print(f'{self.nombre} dice: Guau Gual!!🐕')

        def cumplir_anios(self, enios_add):
                self.edad += enios_add
                print(f'{self.nombre} ahora tiene {self.edad}')
                

p1 = Perro('Rex', 5)     
p1.ladrar() #Rex dice: Guau Gual!!🐕   

p1.cumplir_anios(5) #Rex ahora tiene 6
p1.cumplir_anios(100) #Rex ahora tiene 6


p2 = Perro('Luna', 3) 
p2.ladrar() #Luna dice: Guau Gual!!🐕   
print(p1.nombre) # Rex
print(p2.edad) # 3
p2.edad = -13
print(p2.edad) # 13
print(p2.especie) # Can familiaris
print(Perro.especie) #* Can familiaris

    



#* Métodos (funciones dentro de una clase)
#? Métodos de instancia: 
# Definida dentro de la clase que opera sobre una instancia concreta de esa clase.
# Recibe obligatoriamente el como 1er parámetro "self" 
# que hace referencia al objeto específico que está llamando al método.
# Luego pueden venir más parámetros (o ninguno).
# self no es una palabra reservada. Puedes llamarlo como quieras, pero no lo hagas.
# Para llamar a un método de instancia, primero hay que crear un objeto
# A través de self, el método puede:
# Leer o modificar los atributos de esa instancia.
# Llamar a otros métodos de instancia del mismo objeto.
# Acceder a atributos y métodos de clase (usando self.__class__).



#* 📌 ¿Cuándo usar métodos de instancia?
# Siempre que necesites trabajar con los datos particulares de un objeto (sus atributos).
# Para modificar el estado interno del objeto.
# Para implementar el comportamiento principal de la clase.




# No existe el parámetro cls. El primer parámetro es self, que es la instancia concreta. 
# Por lo tanto, dentro no podemos escribir cls.atributo_de_clase →  porque cls no está definido en ese ámbito.
# Sin embargo, podemos obtener la clase de la siguiente manera:
# nombre_de_clase.atributo_de_clase → Perro.especie
# self.__class__ → devuelve la clase a la que pertenece la instancia.
# type(self) → también devuelve la clase.



#? Métodos de clase: 
# Usan el decorador @classmethod y reciben cls (la clase) como 1er param. 
# Son para Acceder/modificar atributos de clase (compartidos por todas las instancias).
# Pueden Llamar a otros métodos de clase o sobrescribir comportamiento en herencia.
# Pertenece a la clase, no a instancias.
# Se puede llamar:
# Desde la clase: MiClase.mi_metodo_clase(10)
# Desde una instancia: obj = MiClase(); obj.mi_metodo_clase(10) (pero lo común es usarlo desde la clase)


#? Métodos estáticos: 
# Usan @staticmethod y no reciben ni self ni cls. 
# No puede acceder a self ni cls (solo a lo que se le pase)
# Si los necesita, debes pasarlos como parámetro, pero es inusual, 
# porque si necesitas acceder a atributos de clase, mejor usa @classmethod.
# Son funciones de utilidad o cálculos auxiliares relacionadas con la clase, y dentro de ella.
# Simplemente es una función normal, que está "empaquetada" dentro de la clase.
# Se puede llamar:
# √ Desde una instancia: objeto = MiClase(); objeto.mi_metodo_estatico(3, 4)
# √ Desde la clase: MiClase.mi_metodo_estatico(3, 4)




#* SETTERS Y GETTERS
# En Python no es obligatorio, pero se usa cuando necesitas:
# √ Validar datos antes de asignarlos (ej. que una edad no sea negativa).
# √ Controlar si un atributo puede ser leído o modificado.
# √ Mantener la coherencia interna del objeto.
# √ Cambiar la forma interna de almacenar un dato sin afectar el código externo.
#* ✅ La forma pitónica: @property
# Decorador @property y @atributo.setter 
# para crear propiedades que se usan como si fueran atributos normales, pero que ejecutan código metodo getter/setter.

#TODO: Investigar la herencia y polomorfismo.