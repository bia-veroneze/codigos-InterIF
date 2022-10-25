gasolina = input()
gasolina = float(gasolina)

etanol = input()
etanol = float(etanol)

razao = etanol / gasolina

if (razao > 0.7):
  print('GASOLINA')
else:
  print('ETANOL')