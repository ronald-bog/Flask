from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return "Hola Rogelioooozzzzzzz"


@app.route("/procesar2", methods=["POST"])
def procesar2():
    datos = request.json
    dato2 = datos["lenguaje"]
    return dato2
    # return 'Valor recibido y almacenado: {}'.format(dato2)


@app.route("/procesar", methods=["POST"])
def procesar():
    # Obtener datos del cuerpo de la solicitud como un objeto JSON
    datos = request.json

    # Verificar si el campo 'valor' está presente en los datos
    if "lenguaje" in datos:
        # Obtener el valor del campo 'valor'
        valor = datos["lenguaje"]

        # Hacer lo que necesites con el valor (por ejemplo, almacenarlo en una variable)
        mi_variable = valor

        # Devolver una respuesta con el valor procesado
        return jsonify(
            {"mensaje": "Valor recibido y almacenado: {}".format(mi_variable)}
        )
    else:
        # Si el campo 'valor' no está presente en los datos, devolver un error
        return (
            jsonify(
                {"error": 'El campo "valor" no se encontró en los datos enviados.'}
            ),
            400,
        )
