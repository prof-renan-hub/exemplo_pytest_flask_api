def test_listar_produtos_stress(benchmark, client):
    def request_produtos():
        response = client.get("/produtos")
        assert response.status_code == 200
        assert isinstance(response.get_json(), list)

    benchmark.pedantic(request_produtos, iterations=50, rounds=10)

# pytest -s -v --benchmark-only .\tests\stress\stress_bechmark_test.py