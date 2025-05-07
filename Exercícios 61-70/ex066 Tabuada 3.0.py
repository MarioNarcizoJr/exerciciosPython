numero = int(input('Digite um número[-1 para sair]: '))
base = 1
cont = 10
while cont > 0 and numero > 0:
    print(f'{numero} x {base:2} = {numero*base:2}')
    base += 1
    cont -= 1
    if cont == 0:
        cont = 10
        base = 1
        numero = int(input('\nDigite outro número para o cálculo da tabuada [-1 para sair]: '))
print('\nFIM!')
