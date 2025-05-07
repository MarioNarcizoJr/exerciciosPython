from Modulos import moeda

numero = float(input('Digite o preço: R$'))
print(f'\nAumentando em 10% R${moeda.moeda(numero)} , temos R${moeda.moeda(moeda.aumentar(numero))}')
print(f'\nDiminuindo em 5% R${moeda.moeda(numero)} , temos R${moeda.moeda(moeda.diminuir(numero))}')
print(f'\nO dobro de R${moeda.moeda(numero)} é R${moeda.moeda(moeda.dobro(numero))}')
print(f'\nA metade de R${moeda.moeda(numero)} é R${moeda.moeda(moeda.metade(numero))}')



