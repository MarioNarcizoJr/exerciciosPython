numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
maior = 0

print('''
O que deseja fazer com esses dois números:
[1] Somar
[2] Subtrair
[3] Multiplicar
[4] Dividir
[5] Mostrar o maior
[6] Escolher novos números
[7] Sair
''')

opcao = int(input('Digite sua opção: '))

while opcao != 7:
    if opcao < 1 and opcao > 7:
        print('Opção fora dos parâmetros.')
    elif opcao == 1:
        print(f'A soma entre {numero1} + {numero2} é igual = {numero1 + numero2}')
    elif opcao == 2:
        print(f'A subtração entre {numero1} - {numero2} é igual = {numero1 - numero2}')
    elif opcao == 3:
        print(f'A multiplicação entre {numero1} x {numero2} é igual = {numero1 * numero2}')
    elif opcao == 4:
        if numero2 == 0:
            print('Divisão por zero, inválido. Tente novamente.')
        print(f'A divisão entre {numero1} / {numero2} é igual = {numero1 / numero2}')
    elif opcao == 5:
        if numero1 > numero2:
            print(f'O maior número entre {numero1} e {numero2} é {numero1}.')
        elif numero2 > numero1:
            print(f'O maior número entre {numero1} e {numero2} é {numero2}.')
        else:
            print(f'Não há maior numero entre {numero1} e {numero2}.')
    elif opcao == 6:
        numero1 = int(input('Digite um novo valor para o primeiro número: '))
        numero2 = int(input('Digite um novo valor para o segundo número: '))
    opcao = int(input('Digite outra opção: '))
print('Obrigado por utilizar nosso programa.')