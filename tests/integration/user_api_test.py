import json

def test_cria_e_busca_usuario(client):
    # Teste tipo POST /usuario
    payload = {"nome": "Elon", "email": "elon@test.com.br"}
    resp = client.post("/usuario", json=payload)
    assert resp.status_code == 201
    dados = resp.get_json()
    assert dados["nome"] == "Elon"
    assert dados["email"] == "elon@test.com.br"

def test_tcria_e_busca_usuario_fake(client, usuario_fake):
    # Teste tipo POST /usuario
    payload = {"nome": usuario_fake.nome, "email": usuario_fake.email}
    resp = client.post("/usuario", json=payload)
    assert resp.status_code == 201
    dados = resp.get_json()
    assert dados["nome"] == usuario_fake.nome
    assert dados["email"] == usuario_fake.email
    user_id = dados["id"]

    # Test tipo GET /usuario/<id>
    get_resp = client.get(f"/usuario/{user_id}")
    assert get_resp.status_code == 200
    assert get_resp.get_json()["nome"] == usuario_fake.nome
    assert get_resp.get_json()["email"] == usuario_fake.email