entrada = input()

caracter_rancado = []

saida = []
indice = 0

while indice < len(entrada):
  letra = entrada[indice]

  if (letra != '<'):
    saida.append(letra)
  else:
    if (entrada[indice + 1].lower() == 'b'):
      if (entrada[indice + 2] == '>'):
        indice += 2
        caracter_rancado.append(saida.pop())
      else:
        saida.append('<')
    else:
      if (entrada[indice + 1].lower() == 'z'):
        if (entrada[indice + 2] == '>'):
          indice += 2
          saida.append(caracter_rancado.pop())
        else:
          saida.append('<')
      else:
        saida.append('<')
    
  indice += 1

print(''.join(saida))