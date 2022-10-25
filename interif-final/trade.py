entrada = input()

alfabeto_minusculo = 'abcdefghijklmnopqrstuvwxyz'
alfabeto_maiusculo = alfabeto_minusculo.upper()

entrada = entrada.split()
entrada = ''.join(entrada)

saida = ''

for letra in entrada:
  if letra in alfabeto_minusculo:
    saida += '0'
  elif letra in alfabeto_maiusculo:
    saida += '1'

digitos_saida = len(saida) // 8

lista_saida = []

for indice in range(digitos_saida):
  lista_saida.append(saida[indice * 8:indice * 8 + 8])

lista_saida = [int(_, 2) for _ in lista_saida]
lista_saida = [chr(_) for _ in lista_saida if _ != 0]

print(''.join(lista_saida))