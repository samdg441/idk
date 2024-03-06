from flask import Flask, render_template, request
import random

app = Flask(__name__)

nombres = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nuevo_jugador', methods=['POST'])
def nuevo_jugador():
    nombre = request.form['nombre']
    nombres.append(nombre)
    return render_template('bienvenida.html', nombre=nombre)

def obtener_pregunta_aleatoria():
    preguntas = [
        {"pregunta": "¿Cuál es la capital de España?", "respuestas": {"A": "madrid.jpg", "B": "barcelona.jpg", "C": "valencia.jpg", "D": "sevilla.jpg"}, "respuesta_correcta": "A"},
        # Agrega más preguntas aquí
    ]
    pregunta_aleatoria = random.choice(preguntas)
    return pregunta_aleatoria

@app.route('/jugar', methods=['GET', 'POST'])
def jugar():
    if request.method == 'GET':
        pregunta = obtener_pregunta_aleatoria()
        return render_template('jugar.html', pregunta=pregunta)
    else:
        respuesta_usuario = request.form['respuesta']
        # Aquí debes implementar la lógica para verificar la respuesta del usuario
        return render_template('resultado.html')

if __name__ == '__main__':
    app.run(debug=True)
