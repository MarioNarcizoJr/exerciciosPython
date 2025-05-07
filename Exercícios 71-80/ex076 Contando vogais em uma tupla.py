palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')


for palavra in palavras:
    print(f'\nA palavra {palavra} possui as vogais: ', end='')
    for i in palavra:
        if i.lower() in 'aeiou':
            print(i.lower(), end=' ')

print()
print('\nObrigado por utiliar nossos serviços!')
