frase = input('Digite uma frase: ').upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print(f'{inverso} é um palíndromo de {frase}.')
else:
    print(f'{frase}  não é um palíndromo.')
