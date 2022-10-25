entrada = input()
entrada = entrada.split()
entrada = [int(_) for _ in entrada]

entrada_aurora = input()
entrada_aurora = entrada_aurora.split()
entrada_aurora = [int(_) for _ in entrada_aurora]

entrada_breno = input()
entrada_breno = entrada_breno.split()
entrada_breno = [int(_) for _ in entrada_breno]

dicionario_aurora = {}
dicionario_breno = {}
dicionario_aurora2 = {}
dicionario_breno2 = {}

for figurinha in entrada_aurora:
  if figurinha in dicionario_aurora:
    dicionario_aurora[figurinha] += 1
    dicionario_aurora2[figurinha] += 1
  else:
    dicionario_aurora[figurinha] = 1
    dicionario_aurora2[figurinha] = 1

for figurinha in entrada_breno:
  if figurinha in dicionario_breno:
    dicionario_breno[figurinha] += 1
    dicionario_breno2[figurinha] += 1
  else:
    dicionario_breno[figurinha] = 1
    dicionario_breno2[figurinha] = 1

figurinhas_album = list(range(1, entrada[0] + 1))

contagem_aurora = entrada[0]

for figurinha in figurinhas_album:
  if figurinha in list(dicionario_aurora.keys()):
    contagem_aurora -= 1
    dicionario_aurora[figurinha] -= 1

contagem_breno = entrada[0]

for figurinha in figurinhas_album:
  if figurinha in list(dicionario_breno.keys()):
    contagem_breno -= 1
    dicionario_breno[figurinha] -= 1

repetidos_aurora = list(dicionario_aurora2.items())
repetidos_aurora = [_ for _ in repetidos_aurora if _[1] > 1 and _[0] not in dicionario_breno.keys()]

repetidos_aurora = len(repetidos_aurora)

repetidos_breno = list(dicionario_breno2.items())
repetidos_breno = [_ for _ in repetidos_breno if _[1] > 1 and _[0] not in dicionario_aurora.keys()]

repetidos_breno = len(repetidos_breno)

menor = min([repetidos_aurora, repetidos_breno])

contagem_aurora -= menor
contagem_breno -= menor

print(contagem_aurora)
print(contagem_breno)