from random import randint


def sorteia(listo):
	print('Sorteando 5 valores da lista: ', end='')
	for i in range(0, 5):
		listo.append(randint(0, 10))
	for i in listo:
		print(f'{i} ', end='')
	print('Fim!')


def soma_par(lista):
	soma = 0
	print(f'\nSomando os valores pares de {lista}, temos: ', end='')
	for i in lista:
		if i % 2 == 0:
			soma += i
	print(soma)


valores = list()
sorteia(valores)
soma_par(valores)




