entrada = input()
entrada = entrada.split()
entrada = [int(_) for _ in entrada]

[linhas, colunas] = entrada

lista_entrada = [input() for _ in range(linhas)]
lista_entrada = [_.split() for _ in lista_entrada]

lista_palavras = input()
lista_palavras = lista_palavras.split()

palavras_linhas = lista_entrada[::-1][::-1]
palavras_linhas = [''.join(_) for _ in palavras_linhas]

palavras_colunas = []

for x in range(linhas):
  palavra = ''
  for y in range(colunas):
    palavra += lista_entrada[y][x]

  palavras_colunas.append(palavra)

def aparicoes(palavra, frase):
  if (palavra not in frase):
    return 0
  else:
    vezes = 0
    
    for indice in range(len(frase)):
      if frase[indice:indice + len(palavra)] == palavra:
        vezes += 1

  return vezes

dicionario = {}

for palavra in lista_palavras:
  dicionario[palavra] = 0

  for col in palavras_colunas:
    contagem = aparicoes(palavra, col)
    dicionario[palavra] += contagem

  for lin in palavras_linhas:
    contagem = aparicoes(palavra, lin)
    dicionario[palavra] += contagem

for chave in list(dicionario.keys()):
  print(f'{chave}: {dicionario[chave]}')