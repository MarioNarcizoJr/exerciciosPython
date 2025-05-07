print('=' * 50)
print('{:^50}'.format('LOJAS CASAS BAHIA'))
print('=' * 50)

nome = input('Digite o nome do produto: ')
valor = int(input('Qual o valor do produto? R$'))
opcao = input('Deseja continuar[S/N]: ')
menor = valor
total = valor
caros = 0
produto = nome

while opcao in 'sS':
    nome = input('Digite o nome do produto: ')
    valor = int(input('Qual o valor do produto? R$'))
    opcao = input('Deseja continuar[S/N]: ')
    total += valor
    if valor > 1000:
        caros += 1
    if valor < menor:
        produto = nome
        menor = valor
print(f'O total da compra foi R${total} reais.\n'
      f'Temos {caros} produtos custando mais que R$1000.00.\n'
      f'O produto mais barato foi {produto} custando R${menor} reais.')
