
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/hello')
def hello():
    return jsonify({"mensagem": "Olá, mundo!"})

@app.route('/ping')
def ping():
    return jsonify({"status": "ok"})

@app.route('/soma', methods=['POST'])
def soma():
    dados = request.get_json()
    print('dados------------------', dados)
    a = dados.get("a")
    b = dados.get("b")
    return jsonify({"resultado": a + b})

if __name__ == '__main__':
    app.run(debug=True)
