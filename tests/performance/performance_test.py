def test_listar_produtos_performance(benchmark, client):
    def request_produtos():
        response = client.get("/produtos")
        assert response.status_code == 200
        assert isinstance(response.get_json(), list)

    benchmark(request_produtos)

# pytest -s -v --benchmark-only .\tests\performance\performance_test.py