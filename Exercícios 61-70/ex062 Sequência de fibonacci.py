print('SEQUÊNCIA DE FIBONACCI')
termos = int(input('\nDigite a quantidade de termos da sequência de Fibonacci: '))
primeiro = 0
segundo = 1
terceiro = 0
cont = 3
print(f'\n{primeiro} -> {segundo}', end='')

while termos >= cont:
    terceiro = primeiro + segundo
    print(f' -> {terceiro}', end='')
    primeiro = segundo
    segundo = terceiro
    termos -= 1
print(' -> FIM!')
