dados = []
auxi = []

condicao = 's'
maiores = []
menores = []

while condicao != 'n':
    auxi.append(input('Digite o nome: '))
    auxi.append(float(input('Digite o peso: ')))
    dados.append(auxi[:])
    auxi.clear()
    condicao = input('Deseja continuar? [S/N] ').lower()

maior = dados[0][1]
menor = dados[0][1]
maiores.append(dados[0][0])
menores.append(dados[0][0])

for i in range(1, len(dados)):
    if dados[i][1] > maior:
        maiores.clear()
        maiores.append(dados[i][0])
        maior = dados[i][1]
    elif dados[i][1] == maior:
        maiores.append(dados[i][0])
    elif dados[i][1] < menor:
        menores.clear()
        menores.append(dados[i][0])
        menor = dados[i][1]
    elif dados[i][1] == menor:
        menores.append(dados[i][0])

print(f'Ao todo, foram cadastradas {len(dados)} pessoas {dados}.')
print(f'O maior peso foi de {maior}kg. Peso de {maiores}.')
print(f'O menor peso foi de {menor}kg. Peso de {menores}.')
