import math

espacos = input()
espacos = int(espacos)

figurinhas = input()
figurinhas = figurinhas.split()
figurinhas = [int(_) for _ in figurinhas]

flag = False

for figurinha in figurinhas:
  if (figurinha > espacos):
    flag = True

def numero_primo(numero):
  flag = True

  for divisor in range(2, math.ceil(numero / 2) + 1):
    if (divisor != 1 and divisor != numero):
      if (numero % divisor == 0):
        flag = False
  
  return flag

if not flag:
  dicionario_figurinhas = {}

  for figurinha in figurinhas:
    if figurinha in dicionario_figurinhas:
      dicionario_figurinhas[figurinha] += 1
    else:
      dicionario_figurinhas[figurinha] = 1

  sem_repetir = list(dicionario_figurinhas.keys())
  sem_repetir.sort()

  especiais = sem_repetir[::-1][::-1]
  especiais = [_ for _ in especiais if numero_primo(_) and _ != 1]

  sem_repetir = [str(_) for _ in sem_repetir]
  especiais = [str(_) for _ in especiais]

  print(' '.join(sem_repetir))
  print(' '.join(especiais))
else:
  print('ERRO')