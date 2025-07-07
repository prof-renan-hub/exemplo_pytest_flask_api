import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


def fazer_requisicao_get(url):
    """Função para fazer uma única requisição GET."""
    try:
        inicio = time.time()
        response = requests.get(url, timeout=5) # Timeout para evitar pendências
        fim = time.time()
        response.raise_for_status() # Levanta HTTPError para 4XX/5XX responses
        return {
            "status_code": response.status_code,
            "tempo_resposta_ms": (fim - inicio) * 1000,
            "url": url,
            "sucesso": True
        }
    except requests.exceptions.RequestException as e:
        return {
            "status_code": None,
            "tempo_resposta_ms": None,
            "url": url,
            "sucesso": False,
            "erro": str(e)
        }


def simular_carga_paralela(url, num_requests=100, max_workers=10):
    """Simula múltiplas requisições GET paralelas."""
    print(f"Iniciando simulação de {num_requests} requisições paralelas para {url}...")
    resultados = []
    tempo_total_inicio = time.time()
    # Usando ThreadPoolExecutor para paralelismo
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submete as requisições para execução paralela
        future_to_url = {executor.submit(fazer_requisicao_get, url): i for i in range(num_requests)}
        for future in as_completed(future_to_url):
            resultado = future.result()
            resultados.append(resultado)
            if not resultado["sucesso"]:
                print(f"Requisição falhou para {resultado['url']}: {resultado.get('erro')}")
    tempo_total_fim = time.time()
    print(f"Simulação concluída em {tempo_total_fim - tempo_total_inicio:.2f} segundos.")
    # Análise dos resultados
    requisições_bem_sucedidas = [r for r in resultados if r["sucesso"]]
    tempos_resposta = [r["tempo_resposta_ms"] for r in requisições_bem_sucedidas]
    if tempos_resposta:
        print(f"\nResultados:")
        print(f"  Total de requisições: {len(resultados)}")
        print(f"  Requisições bem-sucedidas: {len(requisições_bem_sucedidas)}")
        print(f"  Requisições falhas: {len(resultados) - len(requisições_bem_sucedidas)}")
        print(f"  Tempo de resposta médio: {sum(tempos_resposta) / len(tempos_resposta):.2f} ms")
        print(f"  Tempo de resposta mínimo: {min(tempos_resposta):.2f} ms")
        print(f"  Tempo de resposta máximo: {max(tempos_resposta):.2f} ms")
    else:
        print("Nenhuma requisição bem-sucedida para analisar.")


def simular_carga_comum(url, num_requests=100):
    print(f"Iniciando simulação de {num_requests} requisições comuns para {url}...")
    resultados = []
    tempo_total_inicio = time.time()
    for _ in range(num_requests):
        resultado = fazer_requisicao_get(url)
        resultados.append(resultado)
        if not resultado["sucesso"]:
            print(f"Requisição falhou para {resultado['url']}: {resultado.get('erro')}")

    tempo_total_fim = time.time()
    print(f"Simulação concluída em {tempo_total_fim - tempo_total_inicio:.2f} segundos.")



if __name__ == "__main__":
    # Altere esta URL para a rota da sua API que você deseja testar
    target_url = "http://localhost:5000/produtos"
    # simular_carga_paralela(target_url, num_requests=100, max_workers=20)
    simular_carga_comum(target_url)