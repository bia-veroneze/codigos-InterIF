def fatorial(numero):
  resultado = numero
  
  for numero in range(numero - 1, 1, -1):
    resultado *= numero

  return resultado

quantidade = input()
quantidade = int(quantidade)

repeticoes = int(input())

lista_numeros = [input() for _ in range(repeticoes)]
lista_numeros = [int(_) for _ in lista_numeros]

lista_numeros = [fatorial(_) for _ in lista_numeros]
lista_numeros = [str(_)[0:quantidade] for _ in lista_numeros]
lista_numeros = [int(_) for _ in lista_numeros]

lista_numeros.sort()
print('INICIO')

for numero in lista_numeros:
  print(numero)

print('FIM')