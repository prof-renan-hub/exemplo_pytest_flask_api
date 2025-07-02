def calcular_preco_final(preco_base: float, percentual_desconto: float, imposto_percentual: float) -> float:
    if preco_base < 0 or percentual_desconto < 0 or imposto_percentual < 0:
        raise ValueError("Valores de entrada não podem ser negativos.")
    if percentual_desconto > 1.0:
        raise ValueError("Percentual de desconto não pode ser maior que 100%.")

    preco_apos_desconto = preco_base * (1 - percentual_desconto)
    preco_final = preco_apos_desconto * (1 + imposto_percentual)
    return round(preco_final, 2)





