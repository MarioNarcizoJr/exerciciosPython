from Modulos import moedas3

numero = float(input('Digite o preço: R$'))
print(f'\nAumentando em 10% R${moedas3.moeda(numero)} , temos {moedas3.aumentar(numero, 10, False)}')
print(f'\nDiminuindo em 5% R${moedas3.moeda(numero)} , temos {moedas3.diminuir(numero, 5, True)}')
print(f'\nO dobro de R${moedas3.moeda(numero)} é {moedas3.dobro(numero, False)}')
print(f'\nA metade de R${moedas3.moeda(numero)} é {moedas3.metade(numero, True)}')

