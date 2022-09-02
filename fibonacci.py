from math import *

entrada_dimensao = input()
entrada_dimensao = int(entrada_dimensao)

matriz_entrada = [input() for _ in range(entrada_dimensao)]
matriz_entrada = [_.split() for _ in matriz_entrada]
matriz_entrada = [[int(_) for _ in _a] for _a in matriz_entrada]
# matriz_entrada = [['3', '3', '3', '3', '3', '3', '3'], ['3', '2', '2', '2', '2', '2', '3'], ['3', '2', '1', '1', '1', '2', '3'], ['3', '2', '1', '1', '1', '2', '3'], ['3', '2', '1', '1', '1', '2', '3'], ['3', '2', '2', '2', '2', '2', '3'], ['3', '3', '3', '3', '3', '3', '3']]

if (entrada_dimensao == 1):
  if (matriz_entrada[0][0] == 1):
    print('Fibonacci')
else:
  centro = entrada_dimensao / 2
  centro = floor(centro)

  fileira = matriz_entrada[centro]
  lista = fileira[centro:]

  def pegar_camada(camada, centro, matriz):
    if (camada == 0):
      return [matriz[centro][centro]]
    else:
      tamanho_camada = (camada * 2 - 1) + 2
      comeco = centro - floor(tamanho_camada / 2)
      fim = centro + floor(tamanho_camada / 2)

      topo = matriz[comeco][comeco:fim + 1]
      baixo = matriz[fim][comeco:fim + 1]

      esquerda = []
      direita = []

      for indice in range(comeco + 1, fim):
        esquerda.append(matriz[indice][comeco])
        direita.append(matriz[indice][fim])

      return topo + baixo + esquerda + direita

  camadas = []

  for indice in range(len(lista)):
    camada = pegar_camada(indice, centro, matriz_entrada)
    camadas.append(camada)

  repetiu = True

  for camada in camadas:
    dicionario = {}

    for numero in camada:
      if numero in dicionario:
        dicionario[numero] += 1
      else:
        dicionario[numero] = 1

    if len(list(dicionario.values())) > 1:
      repetiu = False

  if (not repetiu):
    print('Nao fibonacci')
  else:
    lista_fibonacci = [1, 1]

    indice = 2
    while indice < len(lista):
      lista_fibonacci.append(lista_fibonacci[indice - 1] + lista_fibonacci[indice - 2])
      indice += 1

    if lista_fibonacci == lista:
      print('Fibonacci')
    else:
      print('Nao fibonacci')