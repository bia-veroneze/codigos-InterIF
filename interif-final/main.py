entrada = input()

simbolos = [')', '(', 'O', 'D']

aparicoes = 0

for indice in range(len(entrada)):
  if entrada[indice] == ':':
    if indice != 0:
      if entrada[indice - 1] in simbolos:
        aparicoes += 1
    
    if indice != len(entrada) - 1:
      if entrada[indice + 1] in simbolos:
        aparicoes += 1

print(aparicoes)