casa = float(input('Informe o valor da casa que deseja adquirir: '))
salario = float(input('Informe o seu salário: '))
anos = int(input('Informe em quantos anos deseja quitar a compra: '))

if (casa / (anos*12)) > (salario*0.3):
    print(f'EMPRÉSTIMO NEGADO. A pretação mensal de R${(casa / (anos*12)):.2f} reais ultrapassa 30% do seu salário(R${salario*0.3} reais), negócio não pode ser realizado.')
else:
    print(f'EMPRÉSTIMO CONCEDIDO. Parabéns, você pagara R${(casa / (anos*12)):.2f} reais em {anos*12} meses.')
