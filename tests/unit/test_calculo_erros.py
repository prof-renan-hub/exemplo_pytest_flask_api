
import pytest
from calculos.calculos import calcular_preco_final


def test_calculo_com_preco_base_negativo():
    with pytest.raises(ValueError) as ex:
        calcular_preco_final(-10, 0.2, 0.05)
    assert "Valores de entrada não podem ser negativos." in str(ex.value)

def test_calculo_com_desconto_negativo_deve_levantar_valueerror():
    """
    Testa se calcular_preco_final levanta ValueError quando o percentual_desconto é negativo.
    """
    with pytest.raises(ValueError, match="Valores de entrada não podem ser negativos."):
        calcular_preco_final(100, -0.05, 0.05)

def test_calculo_com_imposto_negativo_deve_levantar_valueerror():
    """
    Testa se calcular_preco_final levanta ValueError quando o imposto_percentual é negativo.
    """
    with pytest.raises(ValueError) as excinfo:
        calcular_preco_final(100, 0.1, -0.01)
    assert "Valores de entrada não podem ser negativos." == str(excinfo.value) # Verificação exata da mensagem

def test_calculo_com_desconto_acima_de_100_porcento_deve_levantar_valueerror():
    """
    Testa se calcular_preco_final levanta ValueError quando o percentual_desconto é maior que 1.0 (100%).
    """
    with pytest.raises(ValueError, match="Percentual de desconto não pode ser maior que 100%."):
        calcular_preco_final(100, 1.01, 0.05)

def test_funcao_nao_levanta_erro_para_entradas_validas():
    """
    Verifica que a função não levanta exceções para entradas válidas.
    Um teste que passa aqui significa que nenhuma exceção foi levantada, o que é o esperado.
    """
    resultado = calcular_preco_final(50, 0.2, 0.1) # 50 - 20% = 40; 40 + 10% = 44
    assert resultado == 44.00