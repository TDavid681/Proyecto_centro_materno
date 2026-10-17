# --- AVANCE 1 (PARTE 1) - SUBIDO POR DAVID---
from datetime import datetime

# 1. Definición del Molde
class Tramite:
    def __init__(self, codigo, fecha, tipo, dni, nombre, area, estado):
        self.codigo = codigo
        self.fecha = fecha
        self.tipo = tipo
        self.dni = dni
        self.nombre = nombre
        self.area = area
        self.estado = estado

# 2. Definición del Gestor
class GestorTramites:
    def __init__(self):
        self.lista_tramites = [] 

    # FUNCIONALIDAD BASE 
    def registrar(self, rol):
        if rol == "archivo":
            print("\n[X] Acceso denegado.")
            return
            
        codigo_num = len(self.lista_tramites) + 1
        dni = input("Ingrese DNI: ")
        while dni == "":
            print("[X] Error: Todos los campos son obligatorios.")
            dni = input("Ingrese DNI: ")
        nombre = input("Ingrese Nombres y Apellidos: ")
        while nombre == "":
            print("[X] Error: Todos los campos son obligatorios.")
            nombre = input("Ingrese Nombres y Apellidos: ")
        tipo = input("Tipo (ej. Referencia, SIS): ")
        while tipo == "":
            print("[X] Error: Todos los campos son obligatorios.")
            tipo = input("Tipo (ej. Referencia, SIS): ")
        fecha_actual = datetime.now().strftime("%d/%m/%Y")
        
        nuevo_tramite = Tramite(codigo_num, fecha_actual, tipo, dni, nombre, "Jefatura", "Registrado")
        self.lista_tramites.append(nuevo_tramite)
        print("\n========================================")
        print("          CARGO DE RECEPCION            ")
        print("========================================")
        print(f" Codigo de Tramite : {codigo_num}")
        print(f" Fecha de Ingreso  : {fecha_actual}")
        print(f" Solicitante       : {nombre}")
        print(f" DNI Ciudadano     : {dni}")
        print(f" Tipo de Tramite   : {tipo}")
        print(f" Estado Actual     : Registrado")
        print(f" Area Asignada     : Jefatura")
        print(f" Plazo Estimado    : 3 a 7 dias habiles")
        print("========================================")
        print(f" [OK] Tramite {codigo_num} registrado con exito.")

    # --- ESPACIOS EN BLANCO PARA LOS COMPAÑEROS ---
    def buscar_secuencialmente(self, cod_buscado):
        # TODO: Compañero 2, implementar aquí
        pass
    #AVANCE 3 SUBIDO POR JOSUE CAYAO
    def consultar(self):
        # Módulo de Consulta (Parte 3)
        print("\n=== CONSULTAR TRAMITE ===")
        
        if not self.lista_tramites:
            print("[X] No hay trámites registrados en el sistema.")
            return

        try:
            codigo_buscado = int(input("Ingrese el codigo de tramite a consultar: "))
        except ValueError:
            print("[X] Error: El código debe ser un número entero.")
            return

        # Buscamos el trámite en la lista
        tramite_encontrado = None
        for t in self.lista_tramites:
            if t.codigo == codigo_buscado:
                tramite_encontrado = t
                break

        # Si se encuentra, mostramos sus datos
        if tramite_encontrado:
            print("\n========================================")
            print("          RESULTADO DE CONSULTA         ")
            print("========================================")
            print(f" Codigo de Tramite : {tramite_encontrado.codigo}")
            print(f" Fecha de Ingreso  : {tramite_encontrado.fecha}")
            print(f" Solicitante       : {tramite_encontrado.nombre}")
            print(f" DNI Ciudadano     : {tramite_encontrado.dni}")
            print(f" Tipo de Tramite   : {tramite_encontrado.tipo}")
            print(f" Estado Actual     : {tramite_encontrado.estado}")
            print(f" Area Asignada     : {tramite_encontrado.area}")
            print("========================================")
        else:
            print(f"\n[X] No se encontro ningun tramite con el codigo {codigo_buscado}.")


    def cambiar_estado(self, rol):
        # TODO: Compañero 4, implementar aquí
        print("Módulo de modificación en desarrollo...")

    def reporte_archivo(self):
        # TODO: Compañero 5 , implementar aquí
        print("Módulo de reporte en desarrollo...")

# 3. Flujo Principal del Programa 
def main():
    gestor = GestorTramites()
    
    activo = True
    while activo:
        print("\n=== AUTENTICACION ===")
        print(" [1] Ventanilla \n [2] Jefatura \n [3] Archivo \n [4] Salir")
        opcion_rol = input("Elija una opcion: ")
        
        if opcion_rol == "1": rol = "ventanilla"
        elif opcion_rol == "2": rol = "jefatura"
        elif opcion_rol == "3": rol = "archivo"
        elif opcion_rol == "4": break
        else: continue
            
        sesion = True
        while sesion:
            print(f"\n--- MENU PRINCIPAL [{rol.upper()}] ---")
            print(" 1. Registrar \n 2. Consultar \n 3. Modificar (Solo Jefatura)")
            print(" 4. Reporte Archivo \n 5. Cerrar sesion \n 6. Apagar sistema")
            
            menu = input("Elija (1-6): ")
            
            if menu == "1": gestor.registrar(rol)
            elif menu == "2": gestor.consultar()
            elif menu == "3": gestor.cambiar_estado(rol)
            elif menu == "4": gestor.reporte_archivo()
            elif menu == "5": sesion = False
            elif menu == "6": 
                sesion = False
                activo = False

if __name__ == "__main__":
    main()
