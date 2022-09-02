from pydoc import doc


possibilidades = [
  [0, 0, 1],
  [0, 1, 0],
  [0, 1, 1],
  [1, 0 ,0],
  [1, 0, 1],
  [1, 1, 0],
  [1, 1, 1]
]

entrada_criancas = input()
entrada_criancas = int(entrada_criancas)

entrada_valores = input()
entrada_valores = entrada_valores.split()
entrada_valores = [int(_) for _ in entrada_valores]

doces = []

for possibilidade in possibilidades:
  soma = 0

  for indice in range(3):
    soma += entrada_valores[indice] * possibilidade[indice]

  doces.append(soma)

doces_possiveis = [_ for _ in doces if _ % entrada_criancas == 0]

if (len(doces_possiveis) == 0):
  print('NENHUMA')
  print(0)
else:
  melhor_doce = max(doces_possiveis)
  indice = doces.index(melhor_doce)
  possibilidade = possibilidades[indice]

  resposta = ''

  if (possibilidade[0] == 1):
    resposta += 'A'
  
  if (possibilidade[1] == 1):
    resposta += 'B'

  if (possibilidade[2] == 1):
    resposta += 'C'

  print(resposta)

  print(melhor_doce)