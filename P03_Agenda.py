# Ejercicio: AGENDA


def mostrar_menu():
    print("============================")
    print("********** AGENDA **********")
    print("----------------------------")
    print("Seleccioan una Opción: \n" \
    "1. Agregar Contacto.\n" \
    "2. Buscar Contacto.\n" \
    "3. Mostrar Contactos.\n" \
    "4. Eliminar Contacto.\n" \
    "5. Salir.\n")

def agregar_contacto(agenda):
    print("***** Agregar Contacto *****")
    nombre = input("Nombre y Apellido: ")
    telef_cel = input("N° Tel. Celular: ")
    telef_fijo = input("N° Tel. Fijo: ")
    email = input("Correo Electrónico. ")

    agenda[nombre] = {"telef_cel": telef_cel, "telef_fijo": telef_fijo, "email": email}

    print(f"¡Se ha agregado al contacto {nombre} correctamente!")


def buscar_contacto(agenda):
    print("***** Eliminar Contacto *****")
    nombre = input("Nombre y Apellido: ")
    if nombre in agenda:
        print(f"Nombre: {nombre}")
        print(f"N° Telf. Celular: {agenda[nombre]['telef_cel']}")
        print(f"N° Telf. Fijo: {agenda[nombre]['telef_fijo']}")
        print(f"Correo Electrónico: {agenda[nombre]['email']}")
    else:
        print("El Contacto {nombre} no ha sido encontrado en la Agenda.")


def listar_contactos(agenda):
    if agenda:
        print("Lista de Contactos:")
        for nombre, info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"N° Telf. Celular: {info['telef_cel']}")
            print(f"N° Telf. Fijo: {info['telef_fijo']}")
            print(f"Correo Electrónico: {info['email']}")
            print("-"*30)
    else:
        print("No hay Contactos Registrados!")


def eliminar_contacto(agenda):
    print("***** Eliminar Contacto *****")
    nombre = input("Nombre: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"El Contacto {nombre} se ha eliminado correctamente.")
    else:
        print(f"No se ha encontrado al Contacto {nombre}")

def agenda_contactos():
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input("Opción: ")

        if opcion == "1":
            agregar_contacto(agenda)
            
        elif opcion == "2":
            buscar_contacto(agenda)

        elif opcion == "3":
            listar_contactos(agenda)

        elif opcion == "4":
            eliminar_contacto(agenda)
            
        elif opcion == "5":
            print("Saliendo de la Agenda de Contactos.")
            break
        else:
            print("Opción No Válida! Por favor ingresa un valor entre 1 y 5")
            

agenda_contactos()

