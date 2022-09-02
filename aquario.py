entrada = input()
entrada = entrada.split()
entrada = [int(_) for _ in entrada]

substrato = input()
substrato = int(substrato)

litros = entrada[0] * entrada[1] * entrada[2]
litros /= 1000

kg = entrada[0] * entrada[1] * substrato
kg /= 1000

gota = 0.05
total_gotas = gota * 3 * litros

print(f'{litros:.1f}LTS')
print(f'{kg:.1f}KG')
print(f'{total_gotas:.1f}ML')
