# Práctico 1: Crear un Programa que simule un juego de adivinanza sobre números enteros

import random

def adivinar_numero():
    # Generamos un Número Aleatorio con Random
    numero_secreto = random.randint(1,100)
    intentos = 0
    acierto = False

    print("=================================")
    print("** JUEGO: Adivinando un Número **")
    print("---------------------------------")
    print("Debes Acertar un Número entre 1 y 100")
    print("Vamos.. Intenda Adivinarlo!")
    print("Ganas cuando aciertes en menos intentos.")

    while not acierto:
        # Se solicita el Número entre  1 y 100
        print("---------------------------------")
        print("Introduce un Número entre 1 y 100")
        acertar_numero = input("Número: ")

        # Se verifica que el ingreso sea un Número
        if acertar_numero.isdigit():
            acertar_numero = int(acertar_numero) # Se pasa de texto a entero
            intentos += 1

            if acertar_numero < numero_secreto:
                print(f"El Número Secreto es Mayor a {acertar_numero}")
            elif acertar_numero > numero_secreto:
                print(f"El Número Secreto es Menor a {acertar_numero}")
            else:
                print(f"¡ACERTASTE! Felicitaciones has Ganado!!! El Número Secreto era el {numero_secreto}. Lo lograste en {intentos} intentos.")
                break # ToDo: Corregir y Crear Opción para volver a Jugar de Nuevo.
        else:
            print("Por Favor, Ingresa un Número Válido entre 1 y 100")

adivinar_numero()