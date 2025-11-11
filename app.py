from flask import Flask, jsonify, send_file
import math
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/', methods=['GET'])
def index():
    """Página de bienvenida con input para redirigir a /numero/<n>."""
    return send_file(os.path.join(BASE_DIR, 'index.html'))

@app.route('/numero/<int:n>', methods=['GET'])
def calcular(n):
    factorial = math.factorial(n)
    paridad = "par" if n % 2 == 0 else "impar"
    
    respuesta = {
        "numero_recibido": n,
        "factorial": factorial,
        "paridad": paridad
    }
    
    return jsonify(respuesta)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
