import random
import operator
from time import sleep

dado = dict()

dado['Jogador1'] = random.randint(1, 6)
dado['Jogador2'] = random.randint(1, 6)
dado['Jogador3'] = random.randint(1, 6)
dado['Jogador4'] = random.randint(1, 6)

print('Os valores sorteados foram: ')
for c,v in dado.items():
    print(f'   O {c} tirou {v}.')
    sleep(0.5)

dicionario_ordenado = sorted(dado.items(), key=operator.itemgetter(1))

print()
print('O ranking ficou: ')
c = 1
for i in range(3, -1, -1):
    print(f'   {c}º Lugar {dicionario_ordenado[i][0]} com {dicionario_ordenado[i][1]}.')
    sleep(0.5)
    c += 1
