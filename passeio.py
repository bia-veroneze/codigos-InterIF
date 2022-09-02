entrada_quantidade = input()
entrada_quantidade = int(entrada_quantidade)

entrada_conexoes = [input() for _ in range(entrada_quantidade)]
entrada_conexoes = [_.split() for _ in entrada_conexoes]

def pegar_destinos(conexoes, ponto):
  lista_destinos = []

  for conexao in conexoes:
    if (conexao[0] == ponto):
      lista_destinos.append(conexao[1])
    elif (conexao[1] == ponto):
      lista_destinos.append(conexao[0])

  return lista_destinos

espacos = {}

for conexao in entrada_conexoes:
  for espaco in conexao:
    if (espaco in espacos):
      espacos[espaco] += 1
    else:
      espacos[espaco] = 1

for ponto in list(espacos.keys()):
  rodando = True

  