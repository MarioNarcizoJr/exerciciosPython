frase = input('Digite uma frase: ').strip().lower()
print('A letra a se repete {}.\nA primeira letra a está na posição {}.\n A última letra a está na posição {}.'.format(frase.count('a'), frase.find('a'), frase.rfind('a')))
