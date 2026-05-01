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
        especie = 'Can familiaris' #* Atributos de clase
        def __init__(self, nombre, edad): #todos los metodos de instancia requieren como 1er parametro "self"
                self.nombre = nombre #* Atributos de instancia
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
                

p1 = Perro('Rex', 5)  # *instanciar    
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
#& A través de self, el método puede:
# √ Leer o modificar los atributos de esa instancia.
# √ Llamar a otros métodos de instancia del mismo objeto.
# Acceder a atributos y métodos de clase (usando self.__class__).

#& 📌 ¿Cuándo usar métodos de instancia?
# Para manupular los atributos de los objetos (modificar su estado).
# Para implementar el comportamiento principal de la clase.

class ClienteBancario:
        def __init__(self, titular): #todos los atr que pase por el constructor, debo accdedrlos y modificarloc on self.atributo, y son art de instancia
                self.titular  =  titular
                self.saldo = 0.0 #Atriuto inicial generico.
# vamos a modificar self.saldo con:  depositar, retirar, mostrar_saldo
        def depositar(self, cantidad):
                if cantidad > 0:
                        self.saldo += cantidad
                else: print('No puedes ingresar cantidades negativas')

        def retirar(self, cantidad):
                if cantidad > 0 and self.saldo >= cantidad:
                        self.saldo -= cantidad
                else: print('No puedes retirar mas de lo depositado')
                
        def _verifica_dispo(self, cantidad): #√ Llamar a otros métodos de instancia del mismo objeto.
                if cantidad > 0 and self.saldo >= cantidad: return True
                else: False
        
        def retirar_mejorado(self, cantidad):
                if self._verifica_dispo(cantidad): ## √ Llamar a otros métodos de instancia del mismo objeto.
                        self.saldo -= cantidad
                else: print('No puedes retirar mas de lo depositado')

        def mostrar_saldo(self): #no tiene mas parametros que solo el self!!
                print(f'El cliente {self.titular} - $ {self.saldo}')  

        # def _ultileria() → self.utilteria() 

edily = ClienteBancario('Edily001') #instanciar
adrian = ClienteBancario('adrian001')
edily.depositar(300) #metodo de instancia
print(edily.saldo)
edily.retirar(100)
print(edily.saldo)
edily.mostrar_saldo()
print(print())

adrian.mostrar_saldo()
adrian.depositar(300)
adrian.mostrar_saldo()
adrian.retirar_mejorado(150)
adrian.mostrar_saldo()


#!edily.depositar('n') #metodo de instancia

#& 💡 Parametro cls para metodos de clase
# en metodos de instancia No existe el parámetro cls. El primer parámetro es self, que es la instancia concreta. 
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

class Estudiantes:
        cantidad_estudiantes = 0 #* Atri de clase, para modificarlo o accederlo debes hacerlo con la clase.
        def __init__(self, nombre): #atr de instancia.
                self.nombre = nombre
                Estudiantes.cantidad_estudiantes +=1
        # metodos para get ver, mirar el valor de cantidad_estudiantes y otro metodo para reiniarlo
        @classmethod
        def obtener_total_instancias(cls):
                print(f'La cantidad total de estudiantes instanciados es {cls.cantidad_estudiantes}')
        @classmethod
        def reiniciar_contador_de_estudiantes(cls):
                cls.cantidad_estudiantes = 0
                print(f'La cantidad de estudiantes se reinicio a 0')
                
                

alicia = Estudiantes('Alicia') #instancia, con el constructor instanciamos la clase, tamb se le llaman objetos.
maria = Estudiantes('Maria')
Estudiantes.obtener_total_instancias()   #*2
maria.reiniciar_contador_de_estudiantes() #* La cantidad de estudiantes se reinicio a 
Estudiantes.obtener_total_instancias()    #* La cantidad total de estudiantes instanciados es 0
#los metodos de clase pueden ser llamados por las instancias (inusual) y las clases (lo usual)



#? Métodos estáticos: 
# Usan @staticmethod y no reciben ni self ni cls. 
# No puede acceder a self ni cls, Si los necesita, debes pasarlos como parámetro, pero es inusual, 
# porque si necesitas acceder a atributos de clase, mejor usa @classmethod.
# Son funciones de utilidad o cálculos auxiliares relacionadas con la clase, y dentro de ella.
# Simplemente es una función normal, que está "empaquetada" dentro de la clase.
# Se puede llamar:
# √ Desde una instancia: objeto = MiClase(); objeto.mi_metodo_estatico(3, 4)
# √ Desde la clase: MiClase.mi_metodo_estatico(3, 4)

class Conversor:
        def __init__(self, tipo):
                self.tipo = tipo
                
        @staticmethod #no tienen nada que ver con la clase en si ni las instan por eso no ocupa self ni cls
        def km_a_mil(km):
                return km * 0.621

distancia = Conversor('dictancias')
print(Conversor.km_a_mil(5))
print(distancia.km_a_mil(10))


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

#todo: tarea: crear una clase con atrubutos de instanca privados que requieran getter y getter para su lectura y modificacion