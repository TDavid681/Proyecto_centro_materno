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
            print("\n[X] Acceso denegado: El personal de Archivo no puede registrar trámites.")
            return
            
        codigo_num = len(self.lista_tramites) + 1
        dni = input("Ingrese DNI (8 dígitos obligatorios): ")
        while len(dni) != 8:
            print("[X] Error: El DNI debe tener exactamente 8 dígitos numéricos.")
            dni = input("Ingrese DNI (8 dígitos obligatorios): ")
        nombre = input("Ingrese Nombres y Apellidos: ")
        while nombre == "":
            print("[X] Error: El campo de nombres es obligatorio y no puede estar vacío.")
            nombre = input("Ingrese Nombres y Apellidos: ")
        print("\nTipos de trámite disponibles:")
        print(f" - Referencia")
        print(f" - SIS")
        print(f" - Certificado_Salud")
        print(f" - Descanso_Medico")
        tipo = input("Escriba el tipo de trámite de la lista: ")
        while tipo == "":
            print("[X] Error: El campo de tipo de trámite es obligatorio.")
            tipo = input("Escriba el tipo de trámite de la lista: ")
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

    #Avance - 2 Hecho por Lino
    def buscar_secuencialmente(self, cod_buscado):
        for i in range(len(self.lista_tramites)):
            if self.lista_tramites[i].codigo == cod_buscado:
                return i
        return -1

    def consultar(self):
         # AVANCE-3(PARTE 1) HECHO POR JOSUE CAYAO   
        if len(self.lista_tramites) == 0:
            print("\n[!] No hay trámites registrados en el sistema.")
            return
            
        print("\n--- CÓDIGOS NUMÉRICOS DISPONIBLES ---")
        for t in self.lista_tramites:
            print(f" -> Código: {t.codigo} | Solicitante: {t.nombre}")
            
        buscado = int(input("Ingrese el codigo NUMÉRICO a buscar: "))
        pos = self.buscar_secuencialmente(buscado)
        
        if pos != -1:
            t = self.lista_tramites[pos]
            print("\n--- TRAMITE ENCONTRADO ---")
            print(f"Codigo: {t.codigo} | DNI: {t.dni} | Nombre: {t.nombre}")
            print(f"Tipo: {t.tipo} | Area: {t.area} | Estado: {t.estado}")
        else:
            print("[X] Codigo no encontrado.")

    def cambiar_estado(self, rol):
        # AVANCE-3(PARTE 2) SUBIDO-POR-JUHEN
        if rol != "jefatura":
            print("\n[X] Acceso denegado: Solo Jefatura puede derivar o modificar trámites.")
            return
                    
        if len(self.lista_tramites) == 0:
            print("\n[!] No hay trámites para modificar.")
            return
                    
        print("\n--- CÓDIGOS NUMÉRICOS DISPONIBLES ---")
        for t in self.lista_tramites:
            print(f" -> Código: {t.codigo} | Solicitante: {t.nombre} | Área: {t.area} | Estado: {t.estado}")
                   
                    
        actualizar = int(input("Ingrese el codigo NUMÉRICO a modificar: "))
        pos = self.buscar_secuencialmente(actualizar)
                
        if pos != -1:
            nuevo_estado = input("Escriba el nuevo estado (ej. Atendido, Observado): ")
            while nuevo_estado == "":
                print("[X] Error: El campo de estado es obligatorio.")
                nuevo_estado = input("Escriba el nuevo estado (ej. Atendido, Observado): ")
                    
            nueva_area = input("Escriba la nueva area (ej. Archivo, Medicos): ")
            while nueva_area == "":
                print("[X] Error: El campo de área es obligatorio.")
                nueva_area = input("Escriba la nueva area (ej. Archivo, Medicos): ")
                
            self.lista_tramites[pos].estado = nuevo_estado
            self.lista_tramites[pos].area = nueva_area
            print("\n[OK] Tramite actualizado y derivado correctamente.")
        else:
            print("[X] Codigo no encontrado.")

    #AVANCE-4.1(PARTE 4)Subido por: David Dominguez 
    def eliminar(self, rol):
        # TEMA 3.2: Eliminación
        if rol != "jefatura":
            print("\n[X] Acceso denegado: Solo Jefatura puede eliminar.")
            return
        if len(self.lista_tramites) == 0:
            print("\n[!] No hay trámites para eliminar.")
            return 
        print("\n--- CÓDIGOS NUMÉRICOS DISPONIBLES ---")
        for t in self.lista_tramites:
            print(f" -> Código: {t.codigo} | Solicitante: {t.nombre}") 
        cod = int(input("Ingrese el código NUMÉRICO a eliminar: "))
        pos = self.buscar_secuencialmente(cod)
        
        if pos != -1:
            tramite_eliminado = self.lista_tramites.pop(pos)
            print(f"\n[OK] Trámite {tramite_eliminado.codigo} de '{tramite_eliminado.nombre}' eliminado correctamente.")
        else:
            print("[X] Código no encontrado.")

    def ordenar_por_nombre_burbuja(self):
        n = len(self.lista_tramites)
        if n == 0:
            print("\n[!] No hay trámites para ordenar.")
            return
            
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if self.lista_tramites[j].nombre > self.lista_tramites[j + 1].nombre:
                    self.lista_tramites[j], self.lista_tramites[j + 1] = self.lista_tramites[j + 1], self.lista_tramites[j]
                    
        print("\n[OK] La lista ha sido ordenada alfabéticamente por nombre (Método Burbuja).")
        print("\n--- LISTA ORDENADA POR NOMBRE ---")
        for t in self.lista_tramites:
            print(f" -> Código: {t.codigo} | Nombre: {t.nombre} | Área: {t.area}")

    def mostrar_matriz_bidimensional(self):
        if len(self.lista_tramites) == 0:
            print("\n[!] No hay trámites para mostrar en la matriz.")
            return
            
        matriz = [["CÓDIGO", "DNI", "NOMBRE", "ÁREA", "ESTADO"]]
        
        for t in self.lista_tramites:
            fila = [t.codigo, t.dni, t.nombre, t.area, t.estado]
            matriz.append(fila)
            
        print("\n--- MATRIZ BIDIMENSIONAL DE TRÁMITES ---")
       
        for f in range(len(matriz)):
            fila_str = ""
            for c in range(len(matriz[f])):
                
                fila_str += f"{str(matriz[f][c]):<15}" 
            print(fila_str)
            if f == 0:
                print("-" * 75)

    def reporte_archivo(self):
        # TODO: Compañero 5 , implementar aquí
        print("Módulo de reporte en desarrollo...")

# 3. Flujo Principal del Programa 
def main():
    gestor = GestorTramites()
    
    activo = True
    while activo:
        print("\n=== SISTEMA DE TRÁMITES ===")
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
            print(" 1. Registrar \n 2. Consultar \n 3. Modificar (Solo Jefatura) \n 4. Eliminar (Solo Jefatura)")
            print(" 5. Ordenar por Nombre (Burbuja) \n 6. Ver Matriz Bidimensional")
            print(" 7. Reporte Archivo \n 8. Cerrar sesion \n 9. Apagar sistema")
            
            menu = input("Elija (1-9): ")
            
            if menu == "1": gestor.registrar(rol)
            elif menu == "2": gestor.consultar()
            elif menu == "3": gestor.cambiar_estado(rol)
            elif menu == "4": gestor.eliminar(rol)
            elif menu == "5": gestor.ordenar_por_nombre_burbuja()
            elif menu == "6": gestor.mostrar_matriz_bidimensional()
            elif menu == "7": gestor.reporte_archivo()
            elif menu == "8": sesion = False
            elif menu == "9": 
                sesion = False
                activo = False
            else:
                print("\n[X] Opción inválida. Elija un número del 1 al 9.")
            

if __name__ == "__main__":
    main()