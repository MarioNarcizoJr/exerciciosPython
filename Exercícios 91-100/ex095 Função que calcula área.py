def titulo():
	print('-'*20)
	print('CONTROLE DE TERRENOS')
	print('-'*20)


titulo()
l = float(input('\nLargura(m): '))
c = float(input('Comprimento(m): '))


def area(l, c):
	print(f'\nA área de um terreno {l}x{c} é de {l*c}m².')


area(l, c)
