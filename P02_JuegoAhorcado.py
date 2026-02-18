# Juego del Ahoracado
import random


def obtener_palabra_secreta():
    lenguajes_programacion = ['Python','Javascript','PHP','CSharp','Java','React','Typescript','Angular','Flask','DJango']
    return random.choice(lenguajes_programacion)

def mostrar_progreso(palabra_secreta, letras_adivinadas):
    aciertos = ''

    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            aciertos += letra
        else:
            aciertos += "_"

    return aciertos

def juego_ahorcado():
    lenguaje_secreto = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 3
    juego_terminado = False

    print("Juego del Ahorcado")
    print(f"Tienes {intentos} intentos para Adivinar la Palabra")
    print(mostrar_progreso(lenguaje_secreto, letras_adivinadas), "La Cantidad de letras de la palabra son: ", len(lenguaje_secreto))

    while not juego_terminado and intentos > 0:
        adivinado = input("Ingresa una letra: ").capitalize()

        if len(adivinado) != 1 or not adivinado.isalpha():
            print("Por favor introduzca una letra válida (sólo escribe una letra)")
        elif adivinado in letras_adivinadas:
            print("ya has utilizado esa letra, prueba con otras!")
        else:
            letras_adivinadas.append(adivinado)

            if adivinado in lenguaje_secreto:
                print("¡Muy bien, has Acertado!")
            else:
                intentos -= 1
                print(f"La letra {adivinado} No está en la palabra")
                print(f"Te quedan {intentos} intentos.")

        progreso_actual = mostrar_progreso(lenguaje_secreto, letras_adivinadas)
        print(progreso_actual)

        if "_" not in progreso_actual:
            juego_terminado = True
            lenguaje_secreto = lenguaje_secreto.capitalize()
            print(f"Felicitaciones, has completado la palabra secreta: {lenguaje_secreto}")

    if intentos == 0:
        lenguaje_secreto = lenguaje_secreto.capitalize()
        print(f"Suerte para la Próxima. La Palabra Secreta er: {lenguaje_secreto}")

juego_ahorcado()