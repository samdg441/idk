def solicitar_nombre(jugador):
    nombre = input(f"Ingresa el nombre del jugador número {jugador}: ")
    return nombre

nombres = []
for i in range(1, 11): # Suponiendo que el juego permite hasta 10 jugadores
    nombre = solicitar_nombre(i)
    nombres.append(nombre)

def bienvenida(nombres):
    print("¡Bienvenidos al juego de Quién Quiere Ser Millonario!")
    for i, nombre in enumerate(nombres, start=1):
        print(f"Jugador número {i}: {nombre}")
    print("Las reglas son simples: responde preguntas correctamente y avanza. Tienes la opción de 50/50 y cambiar de pregunta. Puedes retirarte en las estaciones 5 y 7.")

bienvenida(nombres)

import random

def obtener_pregunta_aleatoria():
    # Suponiendo que tienes una lista de preguntas y respuestas
    preguntas = [
        {"pregunta": "¿Cuál es la capital de España?", "respuestas": ["Madrid", "Barcelona", "Valencia", "Sevilla"], "respuesta_correcta": "Madrid"},
        # Agrega más preguntas aquí
    ]
    pregunta_aleatoria = random.choice(preguntas)
    return pregunta_aleatoria

def jugar_pregunta(pregunta):
    print(pregunta["pregunta"])
    for letra, respuesta in zip("ABCD", pregunta["respuestas"]):
        print(f"{letra}. {respuesta}")
    respuesta_usuario = input("Elige una respuesta (A/B/C/D): ")
    return respuesta_usuario == pregunta["respuesta_correcta"]

def jugar():
    for nombre in nombres:
        print(f"Jugador: {nombre}")
        for i in range(10): # 10 estaciones
            pregunta = obtener_pregunta_aleatoria()
            correcto = jugar_pregunta(pregunta)
            if correcto:
                print("¡Correcto!")
                # Aquí puedes implementar el incremento de puntos y las ayudas
            else:
                print("Incorrecto, el juego ha terminado.")
                break

def guardar_resultados(resultados):
    with open("resultados.txt", "w") as archivo:
        for jugador, puntos in resultados.items():
            archivo.write(f"{jugador}: {puntos}\n")

# Ejemplo de uso
resultados = {"Jugador 1": 100, "Jugador 2": 80}
guardar_resultados(resultados)