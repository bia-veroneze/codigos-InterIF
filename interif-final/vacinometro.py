lista_entrada = [input() for _ in range(2)]
lista_entrada = [int(_) for _ in lista_entrada]

razao = lista_entrada[1] / lista_entrada[0]
razao *= 100

print(f'{razao:.1f}%')