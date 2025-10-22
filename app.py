from flask import Flask, jsonify
import math

app = Flask(__name__)


@app.route('/<int:n>', methods=['GET'])
def servicio_factorial(n):
    fact = math.factorial(n)

    etiqueta = "par" if n % 2 == 0 else "impar"

    respuesta = {
        "numero": n,
        "factorial": fact,
        "etiqueta": etiqueta
    }

    return jsonify(respuesta), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)


