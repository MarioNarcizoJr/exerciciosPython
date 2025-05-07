from Modulos import moedas2


numero = float(input('Digite o preço: R$'))
print(f'\nAumentando em 10% R${numero}, temos R${moedas2.aumentar(numero)}')
print(f'\nDiminuindo em 5% R${numero}, temos R${moedas2.diminuir(numero)}')
print(f'\nO dobro de R${numero} é R${moedas2.dobro(numero)}')
print(f'\nA metade de R${numero} é R${moedas2.metade(numero)}')