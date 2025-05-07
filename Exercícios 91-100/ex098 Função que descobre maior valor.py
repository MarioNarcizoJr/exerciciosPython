from random import randint


def maior(lista):
    print(f'{max(lista)}')


valores = []

print('-' * 60)
for i in range(0, 5):
    valores.clear()
    for c in range(0, 5):
        valores.append(randint(0, 20))
    print(f'Analisando os valores passados...')
    for k in range(0, len(valores)):
        print(f'{valores[k]} ', end='')
    print(f'\nO maior valor informado dos {len(valores)} informados foi: ', end='')
    maior(valores)
    print('-' * 60)

print()
print('-' * 60)
print('Obrigado por utilizar nossos serviços.')
print('-' * 60)
