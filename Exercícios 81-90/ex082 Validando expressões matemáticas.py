equacao = input('Digite sua expressão: ')

num1 = equacao.count('(')
num2 = equacao.count(')')

if num1 == num2:
    print('Equação correta!')
    print(num1, num2)
else:
    print('Erro! Equação errada.')
