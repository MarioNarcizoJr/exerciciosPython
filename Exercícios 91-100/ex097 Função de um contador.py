from time import sleep


def contagem(a, b, c):
	if c < 0:
		c *= -1
	if c == 0:
		c = 1
	print(f'Contagem de {a} até {b} de {c} em {c}: ')
	if a < b:
		for i in range(a, b-1, c):
			sleep(0.5)
			print(f'{i}', end=' ')
		print('!')
	else:
		for i in range(a, b-1, -c):
			sleep(0.5)
			print(f'{i}', end=' ')
		print('!')


def linha():
	print('-'*30)



print('Contagem de 1 até 10 de 1 em 1: ')
linha()
for i in range(1, 11):
	sleep(0.5)
	print(f' {i} ', end='')
print('!')
linha()

print('\nContagem de 10 até 0 de 2 em 2: ')
linha()
for i in range(10, -1, -2):
	sleep(0.5)
	print(f'  {i} ', end='')
print('!')
linha()

inicio = int(input('\nInício: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contagem(inicio, fim, passo)