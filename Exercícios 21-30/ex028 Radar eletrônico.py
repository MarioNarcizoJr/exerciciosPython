velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:
    print(f'Você excedeu o limite de velocidade da pista que é 80km. Você sera multado em R${(velocidade - 80)*7} reais.')
else:
    print('Tudo correto com seu veículo. Tenha um bom dia, dirija com segurança.')