lista_entrada = [input() for _ in range(4)]
lista_entrada = [int(_) for _ in lista_entrada]

[x1, v1, x2, v2] = lista_entrada

razao = (x1 - x2) / (v2 - v1)

s = 'SIM'
n = 'NAO'

if x1 < x2:
  if v1 > v2 and razao == int(razao):
    print(s)
  else:
    print(n)
elif x1 > x2:
  if v2 > v1 and razao == int(razao):
    print(s)
  else:
    print(n)
else:
  if v1 == v2:
    print(s)
  else:
    print(n)