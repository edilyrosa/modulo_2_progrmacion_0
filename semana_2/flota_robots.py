
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

from robot import Robot     
class FlotaDeRobots:
    pass

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