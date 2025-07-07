
def login_test(client):
    res = client.post("/login", json={"email": "admin@site.com", "senha": "1234"})
    assert res.status_code == 200
    assert "token" in res.get_json()

def test_hello(client):
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.get_json() == {"mensagem": "Olá, mundo!"}

def test_ping(client):
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}

def test_soma(client):
    resposta = client.post('/soma', json={"a": 3, "b": 7})
    assert resposta.status_code == 200
    json_data = resposta.get_json()
    assert json_data == {"resultado": 10}
