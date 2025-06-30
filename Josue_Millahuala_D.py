"""
Haga un programa que permita generar un menú de gestión de entradas para el la
gira de Rock “los Fortificados” que realizará por distintas locaciones de Chile.
El menú principal debe permitir mostrar 5 opciones:
TOTEM AUTOSERVICIO GIRA ROCK AND CHILE IN CHILE
1.- Comprar entrada a “los Fortificados” en Concepción.✅
2.- Comprar entrada a “los Fortificados” en Puente Alto.✅
3.- Comprar entrada a “los Fortificados” en Muelle Barón en Valparaíso.
4.- Comprar entrada a “los Fortificados” en Muelle Vergara en Viña del Mar.
5.- Salir.
Al ingresar a la opción 4.- Comprar entrada a “los Fortificados” en Muelle Ver-
gara Viña del Mar, se debe permitir ingresar nombre de comprador y tipo de
entrada. Para que la compra sea exitosa se debe cumplir lo siguiente:
a) el nombre de comprador no debe estar repetido,
b) el tipo de entrada solo permite “Sun” (Sunset) o “Ni” (Night),
c) Se maneja un Stock de 50 entradas para esta locación
"""
import re
nuevo_nombre = ""
nombre = {}
def compra_concepcion():
    print("--- Compra en Concepción ---")
    nuevo_nombre = input("Nombre del comprador :")
    if nuevo_nombre in nombre: 
        print("El nombre ya esta registrado.")
        return
    else:
        print("Nombre registrado, Continue con su compra.")

    codigo = input("Ingrese un codigo :")
    if len(codigo) > 6 or not re.search(r"[A-Z]", codigo) or not re.search(r"[0-9]", codigo):
        print("ERROR: El codigo debe tener almenos 6 caracteres, ademas debe contener una mayuscula y un numero.")
        return

    compra_conse = int(input("¿Cuantas entradas deseas comprar? :"))    
    stock = 500

    if compra_conse > stock or compra_conse <= 0:
        print(f"Ingrese un valor entre {stock} y 0.")
    else:
        print("Compra realizada con exito.")
        nombre[nuevo_nombre] = codigo
        stock -= compra_conse
        print("Registro:")
        nombre[nuevo_nombre] = [nuevo_nombre, codigo]
        print ("nombre: ", nombre[nuevo_nombre][0])
        print("codigo: ", nombre[nuevo_nombre][1])
        print(f"stock restante {stock}")
    
def compra_puenteAlto():
    print("--- Puente Alto ---")
    nuevo_nombre = input("Nombre del comprador: ")
    if nuevo_nombre in nombre:
        print("Este nombre ya esta en uso.")
        return
    else:
        print("Nombre registrado, continue con su compra.")
    stock = 1300
    compra_puente = int(input("Cuantas entradas deseas comprar (máximo 3 por persona)"))    
    if compra_puente > 3 or compra_puente <= 0:
        print("Porfavor ingresar un valor entre 0 y 3.")
    else:
        print("Compra realizada correctamente.")
        stock -= compra_puente
        print(f"stock restante {stock}")

def compra_Muelle_valparaiso():
    print("--- Compra Muelle Barón en Valparaíso ---")
    nuevo_nombre = input("Nombre del comprador :")
    if nuevo_nombre in nombre: 
        print("El nombre ya esta registrado.")
        return
    else:
        print("Nombre registrado, Continue con su compra.")
    Codigo = "G"
    stock = 100
    compra_muelle = int(input("Cuantas entradas deseas comprar (máximo 3 por persona): "))    
    if compra_muelle > stock:
        print("No hay stock suficiente.")
    else:
        print("Compra realizada correctamente.")
        stock -= compra_muelle
        print("Registro:")
        nombre[nuevo_nombre] = [nuevo_nombre, Codigo]
        print ("nombre: ", nombre[nuevo_nombre][0])
        print("codigo: ", nombre[nuevo_nombre][1])
        print(f"stock restante {stock}")

def compra_muelle_vina():
    print("--- Compra Muelle Vergara en Viña del Mar ---")
    nuevo_nombre = input("Nombre del comprador :")
    if nuevo_nombre in nombre: 
        print("El nombre ya esta registrado.")
        return
    else:
        print("Nombre registrado, Continue con su compra.")

    codigo = input("Tipo de entrada 'Sun' (Sunset) o 'Ni' (Night): ")
    if codigo not in ("Sun","sun","SUN") or not codigo == ("ni","Ni","NI"):
        print("Porfavor ingresa un tipo de entrada valido.")
        return
    
    stock = 50
    comprar_stock = int(input("Cuanto stock deseas comprar: "))
    if comprar_stock > 50 or comprar_stock <= 0:
        print(f"Ingresar un valor dentro del rango 0 y {stock}.")
    else:
        print("Compra con exito")
        stock -= comprar_stock
        print("Registro:")
        nombre[nuevo_nombre] = [nuevo_nombre, codigo]
        print ("nombre: ", nombre[nuevo_nombre][0])
        print("codigo: ", nombre[nuevo_nombre][1])
        print(f"stock restante {stock}")







def menu():
    opcion = ""
    while opcion != 6:
        print("*** TOTEM AUTOSERVICIO GIRA LOS FORTIFICADOS ROCK AND CHILE IN CHILE ***")

        print("1.-Comprar entrada en Concepción")
        print("2.-Comprar entrada en Puente Alto")
        print("3.-Comprar entrada en Muelle Barón, Valparaíso")
        print("4.-Comprar entrada en Muelle Vergara, Viña del Mar.")
        print("5.-Salir")

        opcion = input("Seleccione una opción :")

        if opcion == "1":
            compra_concepcion()
        elif opcion == "2":
            compra_puenteAlto()
        elif opcion == "3":
            compra_Muelle_valparaiso()
        elif opcion == "4":    
            compra_muelle_vina()
        elif opcion == "5": 
            print("Saliendo del sistema...")
            break       



menu()   