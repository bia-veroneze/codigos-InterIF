entrada = input()

letras = {}

for letra in entrada:
  if letra in letras:
    letras[letra] += 1
  else:
    letras[letra] = 1

lista_quantidades = letras.values()
lista_quantidades = list(lista_quantidades)

if (len(entrada) % 2 == 0):
  flag_impar = False

  for quantidade in lista_quantidades:
    if quantidade % 2 == 1:
      flag_impar = True

  if (flag_impar):
    print(0)
  else:
    print(1)
else:
  bandeiradas_impar = 0

  for quantidade in lista_quantidades:
    if (quantidade % 2 == 1):
      bandeiradas_impar += 1

  if (bandeiradas_impar > 1):
    print(0)
  else:
    print(1)