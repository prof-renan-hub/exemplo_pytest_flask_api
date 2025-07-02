from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from extencoes.ext import db
from model.usuario_model import Usuario

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['TESTING'] = True
db.init_app(app)


@app.route("/usuario", methods=["POST"])
def cria_usuario():
    data = request.get_json()
    usuario = Usuario(nome=data["nome"], email=data["email"])
    db.session.add(usuario)
    db.session.commit()
    return jsonify({"id": usuario.id, "nome": usuario.nome, "email": usuario.email}), 201


@app.route("/usuario/<int:usuario_id>", methods=["GET"])
def buscar_usuario(usuario_id):
    usuario = db.session.execute(db.select(Usuario).where(Usuario.id == usuario_id)).scalar_one()
    if not usuario:
        abort(404, description="Usuário não encontrado")

    return jsonify({
        "id": usuario.id,
        "nome": usuario.nome,
        "email": usuario.email
    }), 200


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data.get("email") == "admin@site.com" and data.get("senha") == "1234":
        return jsonify({"token": "fake-jwt"}), 200
    return jsonify({"erro": "credenciais inválidas"}), 401


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
