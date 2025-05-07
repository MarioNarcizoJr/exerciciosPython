def LeiaInt():
	while True:
		try:
			x = int(input('Digite um número inteiro: '))
		except (ValueError, TypeError):
			print('\n\033[0;31mERRO. Os valores digitados são de um tipo diferente do exigido, por favor tente novamente.\033[m')
			continue
		else:
			return f'\n\033[0;32mO número inteiro digitado foi: {x}\033[m'


def LeiaFloat():
	while True:
		try:
			x = float(input('Digite um número real: '))
		except (ValueError, TypeError):
			print('\n\033[0;31mERRO. Os valores digitados são de um tipo diferente do exigido, por favor tente novamente.\033[m')
			continue
		else:
			return f'\n\033[0;32mO número real digitado foi: {x}\033[m'


inteiro = LeiaInt()
flutuante = LeiaFloat()

print(inteiro)
print(flutuante)
