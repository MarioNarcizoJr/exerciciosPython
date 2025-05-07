numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases númericas para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opcao = int(input('Digite sua opção: '))
if opcao > 3 or opcao < 1:
    print('Erro, sua opção está fora dos parâmetros.')
elif opcao == 1:
    print(f'O número {numero} em binário é {bin(numero)}.')
elif opcao == 2:
    print(f'O número {numero} em octal é {oct(numero)}.')
else:
    print(f'O número {numero} em hexadecimal é {hex(numero)}.')
