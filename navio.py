lista_entrada = []
# lista_entrada = [3, 2, 2, 0, 3, 1, 0, 0, 1]
esperando_entrada = True

while esperando_entrada:
  entrada = input()
  entrada = int(entrada)
  
  if (entrada == -1):
    esperando_entrada = False
  else:
    lista_entrada.append(entrada)

lista_final = []

for item in lista_entrada:
  if (item == 1 or item == 2 or item == 3):
    lista_final.append(item)
  elif (item == 0):
    lista_final.pop()

if (len(lista_final) > 0):
  for item in lista_final:
    print(item)
else:
  print(-1)