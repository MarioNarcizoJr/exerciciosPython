def fatorial(x, show=False):
    """
    Função para calcular o fatorial em que se pode ver o cálculo ou não.
    :param x: Número que será calculado o fatorial
    :param show: Parâmetro opcional que determina se o cálculo será mostrado ou não.
    :return: Valor do fatorial de X
    Função Criada por Mário Narcizo 13/07/2021
    """
    auxiliar = 1
    numero = x
    if show:
        while x != 0:
            auxiliar *= x
            if x > 1:
                print(f'{x} x ', end='')
            elif x == 1:
                print(f'{x} = ', end='')
            x -= 1
        return auxiliar
    elif not show:
        while x != 0:
            auxiliar *= x
            x -= 1
        return f'O fatorial de {numero} é igual à: {auxiliar}.'


valor = int(input('Digite o número que deseja calcular o fatorial: '))
condicao = int(input('Quer ver o cálculo? Digite 1 se sim ou 0 senão: '))

if condicao == 1:
    calculo = True
else:
    calculo = False

print(fatorial(valor, calculo))

#OUTRA FORMA MAIS SIMPLES DE SE FAZER O CÓDIGO PRINCIPAL
"""for i in range(x, 0, -1):
	if show:
		print(i, end='')
		if i > 1:
			print(' x ', end='')
		else:
			print(' = ', end='')
	auxiliar *= i
return auxiliar"""