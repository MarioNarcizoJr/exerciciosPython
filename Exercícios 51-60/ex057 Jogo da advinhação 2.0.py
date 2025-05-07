import random
aleatorio = random.randint(0,10)
print('-='*15)
print('JOGO DA ADVINHAÇÃO')
print('-='*15)
print('Pensei em um número de 0 a 10, tente ganhar de mim...')
numero = int(input('Digite o número que você acha: '))
palpites = 1

while aleatorio != numero:
    if aleatorio > numero:
        numero = int(input('Errou, seu número foi baixo, tente novamente: '))
    else:
        numero = int(input('Errou, seu número foi alto, tente novamente: '))
    palpites += 1
print(f'Parabéns, você acertou em {palpites} tentativas. Pensei no número {aleatorio}.')
