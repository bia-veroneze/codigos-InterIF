entrada_lista = []

while True:
  try:
    entrada = input()
    entrada = int(entrada)
    entrada_lista.append(entrada)
  except EOFError:
    break

def processo(numero):
  vezes = 0

  while numero != 1:
    if (numero % 2 == 0):
      numero //= 2
      vezes += 1
    else:
      numero *= 3
      numero += 1
      vezes += 1
  
  return vezes

entrada_lista = [processo(_) for _ in entrada_lista]

for resposta in entrada_lista:
  print(resposta)