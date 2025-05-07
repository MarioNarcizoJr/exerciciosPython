salario = float(input('Digite o valor de seu salário: R$'))
if salario > 1250:
    print(f'Parabéns você acaba de receber um aumento de 10%, seu novo salário será R${salario + (salario * 0.1)} reais.')
else:
    print(f'Parabéns você acaba de receber um aumento de 15%, seu novo salário será R${salario + (salario * 0.15)} reais.')
