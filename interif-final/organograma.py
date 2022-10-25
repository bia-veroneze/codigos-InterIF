titulo = input()

rodando = True

estrutura = {}

while rodando:
  entrada = input()
  if (entrada == 'fim entrada'):
    rodando = False
  else:
    entrada = entrada.split()

    if entrada[1] in estrutura:
      estrutura[entrada[1]].append(entrada[0])
    else:
      estrutura[entrada[1]] = [entrada[0]]

alvo = input()
bagulhos = []
resposta = []

def procurar(palavra):
  if palavra in estrutura:
    conteudos = estrutura[palavra]
    
    for conteudo in conteudos:
      bagulhos.append(conteudo)
      
    procurar(conteudo)

procurar(alvo)
print(alvo)
print(bagulhos)