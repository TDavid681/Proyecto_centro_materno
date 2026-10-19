# --- AVANCE 1 (PARTE 1) - SUBIDO POR DAVID---
from datetime import datetime

# 1. Definición del Molde
class Tramite:
    def __init__(self, codigo, fecha, tipo, dni, nombre, apellido, area, estado):
        self.codigo = codigo
        self.fecha = fecha
        self.tipo = tipo
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.area = area
        self.estado = estado

# 2. Definición del Gestor
class GestorTramites:
    def __init__(self):
        self.lista_tramites = []
        self.contador_codigos = 1 

    # FUNCIONALIDAD BASE 
    def registrar(self, rol):
        if rol == "archivo":
            print("\n[X] Acceso denegado: El personal de Archivo no puede registrar trámites.")
            return
            
        codigo_num = self.contador_codigos
        self.contador_codigos += 1
        dni = input("Ingrese DNI (8 dígitos obligatorios): ")
        while len(dni) != 8:
            print("[X] Error: El DNI debe tener exactamente 8 dígitos numéricos.")
            dni = input("Ingrese DNI (8 dígitos obligatorios): ")
        nombre = input("Ingrese Nombres: ")
        while nombre == "":
            print("[X] Error: El campo de nombres es obligatorio y no puede estar vacío.")
            nombre = input("Ingrese Nombres: ")
        apellido = input("Ingrese Apellidos: ")
        while apellido == "":
            print("[X] Error: El campo de apellidos es obligatorio y no puede estar vacío.")
            apellido = input("Ingrese Apellidos: ")
        tipo = ""
        while tipo != "Referencia" and tipo != "SIS" and tipo != "Certificado_Salud" and tipo != "Descanso_Medico":
            print("\nTipos de trámite disponibles:")
            print(f" 1. Referencia")
            print(f" 2. SIS")
            print(f" 3. Certificado_Salud")
            print(f" 4. Descanso_Medico")
            entrada = input("Escriba el tipo de trámite de la lista(1-4): ")
            if entrada == "1":
                tipo = "Referencia"
            elif entrada == "2":
                tipo = "SIS"
            elif entrada == "3":
                tipo = "Certificado_Salud"
            elif entrada == "4":
                tipo = "Descanso_Medico"
            else:
                print("[X] Error: Tipo de trámite inválido o vacío. Intente nuevamente.")
        requisitos = input("\n¿El ciudadano cumple con todos los requisitos? (si/no): ")
        while requisitos != "si" and requisitos != "no":
            print("[X] Error: Responda únicamente 'si' o 'no' (en minúsculas).")
            requisitos = input("¿El ciudadano cumple con todos los requisitos? (si/no): ")
        if requisitos == "no":
            print("\n[!] Registro cancelado: El trámite no puede proceder sin los requisitos completos.")
            self.contador_codigos -= 1 
            return
        fecha_actual = datetime.now().strftime("%d/%m/%Y")
        
        nuevo_tramite = Tramite(codigo_num, fecha_actual, tipo, dni, nombre, apellido, "Jefatura", "Registrado")
        self.lista_tramites.append(nuevo_tramite)
        print("\n========================================")
        print("          CARGO DE RECEPCION            ")
        print("========================================")
        print(f" Codigo de Tramite : {codigo_num}")
        print(f" Fecha de Ingreso  : {fecha_actual}")
        print(f" Solicitante       : {nombre} {apellido}")
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
            
        self.ordenar_por_nombre_burbuja()
        self.mostrar_matriz_bidimensional()
        
            
        buscado = int(input("Ingrese el codigo NUMÉRICO a buscar: "))
        pos = self.buscar_secuencialmente(buscado)
        
        if pos != -1:
            t = self.lista_tramites[pos]
            print("\n--- TRAMITE ENCONTRADO ---")
            print(f"Codigo: {t.codigo} | DNI: {t.dni} | Nombre: {t.nombre} {t.apellido}")
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
                    
        self.ordenar_por_nombre_burbuja()
        self.mostrar_matriz_bidimensional()
                   
                    
        actualizar = int(input("Ingrese el codigo NUMÉRICO a modificar: "))
        pos = self.buscar_secuencialmente(actualizar)
                
        if pos != -1:
            nuevo_estado = ""
            while nuevo_estado != "En evaluacion" and nuevo_estado != "Denegado" and nuevo_estado != "Aprobado":
                print("\nEstados disponibles:")
                print(f" 1. En evaluacion")
                print(f" 2. Denegado")
                print(f" 3. Aprobado")
                entrada_estado = input("Escriba el número del estado para el trámite (1-3): ")
                if entrada_estado == "1":
                    nuevo_estado = "En evaluacion"
                elif entrada_estado == "2":
                    nuevo_estado = "Denegado"
                elif entrada_estado == "3":
                    nuevo_estado = "Aprobado"
                else:
                    print("[X] Error: Estado inválido o vacío. Intente nuevamente.")
            nueva_area = ""
            while nueva_area != "Archivo" and nueva_area != "Medico Jefe" and nueva_area != "Diris Lima norte" and nueva_area != "Hospital Referencia":
                print("\nAreas disponibles:")
                print(f" 1. Archivo")
                print(f" 2. Medico Jefe")
                print(f" 3. Diris Lima norte")
                print(f" 4. Hospital Referencia")
                entrada_area = input("Escriba el número del área para derivar el trámite (1-4): ")
                if entrada_area == "1":
                    nueva_area = "Archivo"
                elif entrada_area == "2":
                    nueva_area = "Medico Jefe"
                elif entrada_area == "3":
                    nueva_area = "Diris Lima norte"
                elif entrada_area == "4":
                    nueva_area = "Hospital Referencia"
                else:
                    print("[X] Error: Área inválida o vacía. Intente nuevamente.")
                    
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
        self.ordenar_por_nombre_burbuja()
        self.mostrar_matriz_bidimensional()
        cod = int(input("Ingrese el código NUMÉRICO a eliminar: "))
        pos = self.buscar_secuencialmente(cod)
        
        if pos != -1:
            tramite_eliminado = self.lista_tramites.pop(pos)
            print(f"\n[OK] Trámite {tramite_eliminado.codigo} de '{tramite_eliminado.nombre}' eliminado correctamente.")
        else:
            print("[X] Código no encontrado.")

    def ordenar_por_nombre_burbuja(self):
        n = len(self.lista_tramites)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if self.lista_tramites[j].nombre > self.lista_tramites[j + 1].nombre:
                    self.lista_tramites[j], self.lista_tramites[j + 1] = self.lista_tramites[j + 1], self.lista_tramites[j]

    def mostrar_matriz_bidimensional(self):
        if len(self.lista_tramites) == 0:
            print("\n[!] No hay trámites registrados para mostrar.")
            return
        matriz = [["CÓDIGO", "DNI", "NOMBRE","APELLIDO", "ÁREA", "ESTADO", "TIPO"]]
        
        for t in self.lista_tramites:
            fila = [t.codigo, t.dni, f"{t.nombre}", f"{t.apellido}", t.area, t.estado,t.tipo]
            matriz.append(fila)
            
        print("\n--- TRÁMITES DISPONIBLES ---")
        for f in range(len(matriz)):
            fila_str = ""
            for c in range(len(matriz[f])):
                fila_str += f"{str(matriz[f][c]):<20}" 
            print(fila_str)
            if f == 0:
                print("-" * 140)
   #AVANCE-5(Parte5)SUBIDO POR: Rodrigo Escudero
    def reporte_archivo(self):
        print("\n--- REPORTE DE ARCHIVO ---")
        contador = 0
        for t in self.lista_tramites:
            if t.area == "Archivo":
                contador += 1
                print(f"Tramite: {t.codigo} | Solicitante: {t.nombre} {t.apellido} | Estado: {t.estado} | Tipo: {t.tipo}")
        print(f"Total en Archivo: {contador}")

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
        elif opcion_rol == "4":
            print("\nSaliendo del sistema. ¡Hasta luego!") 
            break
        else:
            print("\n[X] Opción inválida. Elija un número del 1 al 4.") 
            continue
            
        sesion = True
        while sesion:
            print(f"\n--- MENU PRINCIPAL [{rol.upper()}] ---")
            print(" 1. Registrar \n 2. Consultar \n 3. Modificar (Solo Jefatura) \n 4. Eliminar (Solo Jefatura)")
            print(" 5. Reporte Archivo \n 6. Mostrar Trámites \n 7. Cerrar sesion \n 8. Apagar sistema")
            
            menu = input("Elija (1-8): ")
            
            if menu == "1": gestor.registrar(rol)
            elif menu == "2": gestor.consultar()
            elif menu == "3": gestor.cambiar_estado(rol)
            elif menu == "4": gestor.eliminar(rol)
            elif menu == "5": gestor.reporte_archivo()
            elif menu == "6": gestor.mostrar_matriz_bidimensional()
            elif menu == "7": sesion = False
            elif menu == "8":
                print("\n[i] Apagando el sistema por completo.") 
                sesion = False
                activo = False
            else:
                print("\n[X] Opción inválida. Elija un número del 1 al 8.")
                
if __name__ == "__main__":
    main()