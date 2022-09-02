entrada_quantidade = input()
entrada_quantidade = int(entrada_quantidade)

entrada_figurinhas = input()
entrada_figurinhas = entrada_figurinhas.split()
entrada_figurinhas = [int(_) for _ in entrada_figurinhas]

maior = max(entrada_figurinhas)

if maior > entrada_quantidade:
  print('ERRO')
else:
  dicionario_figurinhas = {}

  for figurinha in entrada_figurinhas:
    if (figurinha not in dicionario_figurinhas.keys()):
      dicionario_figurinhas[figurinha] = 1
    else:
      dicionario_figurinhas[figurinha] += 1

  figurinhas_nao_repetidas = dicionario_figurinhas.keys()


  figurinhas_especiais = []

  for figurinha in figurinhas_nao_repetidas:
    palavra = str(figurinha)
    ultimo_numero = palavra[len(palavra) - 1]

    if (ultimo_numero == '3'):
      figurinhas_especiais.append(figurinha)


  repetidas = [_ for _ in dicionario_figurinhas.values() if _ != 1]
  for idx in range(len(repetidas)):
    repetidas[idx] -= 1
  repetidas = sum(repetidas)


  indices_especiais = []

  for figurinha in figurinhas_especiais:
    indice = list(dicionario_figurinhas.keys()).index(figurinha)
    indices_especiais.append(indice)

  especiais_quantidade = [list(dicionario_figurinhas.values())[_] for _ in indices_especiais]

  especiais_repetidos_quantidade = [_ for _ in especiais_quantidade if _ != 1]

  for idx in range(len(especiais_repetidos_quantidade)):
    especiais_repetidos_quantidade[idx] -= 1
  especiais_repetidos_quantidade = sum(especiais_repetidos_quantidade)

  print(f'{len(figurinhas_nao_repetidas)} {len(figurinhas_especiais)} {repetidas} {especiais_repetidos_quantidade}')