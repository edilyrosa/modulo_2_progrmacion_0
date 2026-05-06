
# ============================================
#*  MODULARIDAD EN PYTHON — flota_robots.py
# ============================================

#* ¿Qué es la modularidad?
# ┌──────────────────────────────────────────────────────────────────────┐
# │  Dividir el código en archivos separados donde cada uno tiene        │
# │  UNA responsabilidad clara.                                          │
# │                                                                      │
# │   robot.py        → sabe QUÉ es un Robot (su molde/clase)            │
# │   flota_robots.py → sabe GESTIONAR una colección de robots           │
# │                                                                      │
# │  FlotaDeRobots NECESITA a Robot para existir.                        │
# │  Sin el import, este archivo no puede funcionar. Eso es              │
# │  una dependencia lógica — la forma correcta de modularizar.          │
# └──────────────────────────────────────────────────────────────────────┘

from robot import Robot, PI_2    
class FlotaDeRobots:
    # aqui podria exi art de clase
    #? Constructor
    def __init__(self, nombre_empresa):
        self.nombre_empresa = nombre_empresa
        self.robots = [] #Lista de los robots de la flota
    
    #? metodos
    def agregar_robot(self, nombre, tarea):
        nuevo_robot = Robot(nombre, tarea)
        self.robots.append(nuevo_robot)
        print(f'➕Se agrego el robot {nombre} en la flota {self.nombre_empresa}')
        
    def saludar_todos_activos(self):
        activos = [ r for r in self.robots if r.activo] #TODO: Listas comprehension
        print(f'{self.nombre_empresa} - tiene {len( activos)} robots activos!!')
        for robot in activos:
            robot.saludar() #estamos llamado a un metodo de la clase Robot()
        
    def apagar_robot(self, nombre):
        for r in self.robots:
            if r.nombre == nombre:
                r.apagar()
                return
        print(f'⚠️ No se encontro robots con el nombre {nombre}')
    
    def mostrar_estado(self):
        print(f'\n\nESTADO DE LOS ROBOTS DE LA FLOTA { self.nombre_empresa}')
        for robot in self.robots:
            robot.estado() #estamos llamado a un metodo de la clase Robot()
    
    def resumen(self):
        total = len(self.robots)
        activos = sum(1 for r in self.robots if r.activo)
        print(f'\n Resumen: total robots: {total} | {activos} Activos | {total - activos} Inactivos')
        
        
        
        
armada_americana = FlotaDeRobots('Armada Americana!!')
armada_rusa = FlotaDeRobots('Armada Rusa!!')
armada_americana.agregar_robot('Robotina 1', 'canta para america')
armada_americana.agregar_robot('Robotina 2', 'andar para america')
armada_americana.agregar_robot('Robotina 3', 'limpiar para america')

armada_americana.saludar_todos_activos()
armada_americana.apagar_robot('Robotina 1')
armada_americana.saludar_todos_activos()
armada_americana.mostrar_estado()
armada_americana.resumen()






#& ─────────────────────────────────────────────────────────────────────
#& CONCLUSIÓN SOBRE MODULARIDAD:
#&
#&  robot.py         → módulo REUTILIZABLE en cualquier proyecto
#&  flota_robots.py  → módulo que DEPENDE de robot.py lógicamente
#&
#&  Esta misma estructura la veremos en el proyecto de emails:
#&   enviador_correo.py  → clase que sabe enviar un correo
#&   envio_automatico.py → programa que usa esa clase para automatizar
#& ─────────────────────────────────────────────────────────────────────