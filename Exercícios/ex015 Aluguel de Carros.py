quilometros = float(input('Digite a quantidade de Km rodados com o carro: '))
dias = int(input('Digite a quantidade de dias que o carro passou alugado: '))
print(f'Obrigado por utilizar nossos serviços, total a pagar é de R${(quilometros*0.15) + (dias * 60):.2f}.')
