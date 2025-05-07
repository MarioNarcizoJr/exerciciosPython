numero = int(input('Digite um número inteiro entre 0 e 9999: '))
print(f'O número {numero} tem:\n{numero % 10} unidades\n{numero // 10 % 10} dezenas\n{numero // 100 % 10} centenas\n{numero // 1000 % 10} milhares.')
