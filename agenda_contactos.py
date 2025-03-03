def mostrar_menu():
    print("\nAgenda de contactos")
    print("1. Agregar nuevo contacto")
    print("2. Eliminar un contacto")
    print("3. Buscar contacto")
    print("4. Lista de contactos")
    print("5. Salir del programa")
    print("\n")

def agregar_contactos(agenda):
    nombre = input("Ingrese el nombre y apellido del contacto: ")
    telefono = input("Ingrese el telefono del contacto: ")
    email = input("Ingrese el email del contacto: ")
    agenda[nombre] = {"telefono": telefono, "email": email}
    print(f"Se ha agregado el contacto {nombre} exitosamente!")
    
def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"El contacto {nombre} ha sido borrado correctamente.")
    else:
        print(f"No se encontró el contacto {nombre}")

def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto que desea buscar: ")
    if nombre in agenda:
        print(f"Nombre: {nombre}")
        print(f"Telefono: {agenda[nombre]["telefono"]}") #Como tengo que buscar por key, en este caso el telefono, ademas de usar [] para el nombre, tengo que pasarle otra key para el telefono
        print(f"Email: {agenda[nombre]["email"]}")
    else:
        print(f"El contacto {nombre} no fue encontrado en la agenda")
        

def listar_contactos(agenda):
    if agenda:
        print("\nLista de contactos: ")
        for nombre, info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Telefono: {info["telefono"]}") #Como yo ya tengo la informacion directa, paso la key []
            print(f"Nombre: {info["email"]}")
            print("\n")
    else: 
        print("La agenda aun está vacía.")
            
            
            
    
        

def agenda_contactos():
    agenda = {}
    
    while True:
        mostrar_menu()
        opcion = input("Por favor elija una opcion: ")
        print("\n")
        
        if opcion == "1":
            agregar_contactos(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            listar_contactos(agenda) 
        elif opcion == "5":
            print("Saliendo de la agenda de contactos. Hasta luego")
            break
        else:
            print("Por favor, seleccione una opción válida.")
            
agenda_contactos()