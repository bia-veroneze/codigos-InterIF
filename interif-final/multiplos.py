entrada = input()

par = []
impar = []

for digito in entrada:
  if int(digito) % 2 == 0:
    par.append(digito)
  else:
    impar.append(digito)

def divisivel(numero):
  return numero % 3 == 0

par = [int(_) for _ in par]
impar = [int(_) for _ in impar]

soma_par = sum(par)
soma_impar = sum(impar)

if (divisivel(soma_par)):
  print('S')
else:
  print('N')

if (divisivel(soma_impar)):
  print('S')
else:
  print('N')