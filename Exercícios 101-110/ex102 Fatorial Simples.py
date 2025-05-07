def fatorial(x):
    """
    Função para o cálculo de fatorial:
    :param x: Valor para o qual será calculado o fatorial
    :return: Valor final
    Função criada por Mário Narcizo 13/07/2021
    """
    valor = 1
    numero = x
    if x == 0:
        return 'Opção Inválida, execute novamente o programa!'
    else:
        while x != 1:
            valor *= x
            x -= 1
    return f'O fatorial de {numero} é igual à: {valor}'


resultado = int(input('Digite o valor que deseja saber o fatorial: '))
print()
print(fatorial(resultado))
