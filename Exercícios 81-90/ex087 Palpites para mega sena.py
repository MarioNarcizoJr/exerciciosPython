import random
from time import sleep

print('_'*60)
print('{:^60}'.format('JOGO DA MEGA SENA'))
print('-'*60)

jogos = int(input('\nQuantos jogos deseja ver: '))
lista = []

for i in range(0, jogos):
    for c in range(0,6):
        aleatorio = random.randint(1, 60)
        if aleatorio not in lista:
            lista.append(aleatorio)
        elif aleatorio in lista:
            aleatorio = random.randint(1, 60)
            lista.append(aleatorio)
    sleep(1)
    print(f'\nO {i+1}º jogo é: {lista}')
    lista.clear()
print('-'*60)
print(f'\nObrigado por utilizar nossos serviços!')
