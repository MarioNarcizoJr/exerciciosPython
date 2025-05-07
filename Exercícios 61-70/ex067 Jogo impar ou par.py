import random

print('-='*15)
print('JOGO DO PAR OU IMPAR')
print('-='*15)

valor = computador = 0
opcao = ''
soma = vitorias = derrotas = 0

while valor >= 0:
    computador = random.randint(0, 10)
    valor = int(input('\nDigite um valor: '))
    if valor < 0:
        break
    opcao = input('Par ou ímpar[P/I]: ')
    soma = valor + computador
    if soma % 2 == 0:
        if opcao in 'pP':
            print(f'\nParabéns, você escolheu Par e o valor foi {soma}.')
            vitorias += 1
        else:
            print(f'\nPerdeu, você escolheu ímpar e o valor foi {soma}.')
            derrotas += 1
    else:
        if opcao in 'iI':
            print(f'\nParabéns, você escolheu Ímpar e o valor foi {soma}.')
            vitorias += 1
        else:
            print(f'\nPerdeu, você escolheu par e o valor foi {soma}.')
            derrotas += 1
print(f'Obrigado por jogar você venceu {vitorias} vezes e perdeu {derrotas} vezes, volte sempre.')
