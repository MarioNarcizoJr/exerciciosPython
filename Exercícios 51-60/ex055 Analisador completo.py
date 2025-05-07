soma = mulheres = 0
nomevelho = ''
maiorid = 0

for cont in range(1, 5):
    print(f'-=-=-= {cont}º Pessoa -=-=-=')
    nome = input(f'Nome: ')
    idade = int(input(f'Idade: '))
    sexo = input(f'Sexo[M/F]: ')
    soma += idade
    if sexo in 'Mm':
        if idade > maiorid:
            maiorid = idade
            nomevelho = nome
        
    if sexo in 'Ff':
        if idade < 20:
            mulheres += 1

print(f'A média de idade entre os participante é de {soma / 4:.2f} anos.\n'
      f'O homem mais velho tem {maiorid} e se chama {nomevelho}.\n'
      f'Existem {mulheres} mulheres menores de 20 anos.')
