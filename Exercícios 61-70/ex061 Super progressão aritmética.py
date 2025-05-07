termo1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
novotermo = 1
pa = termo1 + 9*razao
qtd = 10
cont = 10

while cont > 0:
    print(f'{termo1} -> ', end='')
    termo1 += razao
    cont -= 1
    if cont == 0:
        print('Pausa')
        cont = int(input('Quantos termos a mais você quer: '))
        qtd += cont
print(f'Progressão finalizada, foram printados na tela {qtd} valores.')
