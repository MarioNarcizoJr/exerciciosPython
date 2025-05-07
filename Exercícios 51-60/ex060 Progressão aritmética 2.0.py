termo1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
pa = termo1 + 9*razao
cont = 10

while cont > 1:
    print(f'{termo1} -> ', end='')
    termo1 += razao
    cont -= 1

print(pa)