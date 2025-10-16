def count_negatives(values):
    negativos = 0
    for v in values[:10]:  # garante que pegamos no máximo 10 valores
        if v < 0:
            negativos += 1
    return negativos

# Exemplo de uso:
entrada = [5, -2, 0, -7, 3, -1, 8, -4, 9, -6]  # 5 negativos
print("Negativos:", count_negatives(entrada))