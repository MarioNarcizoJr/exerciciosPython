from time import sleep

print('~' * 30)
print(f'\033[0;32m{"SISTEMA DE AJUDA PyHELP":^30}\033[m')
print('~' * 30)

funcao = input('\n\033[0;34mFunção ou Biblioteca > \033[m')

while funcao != 'fim':
    print()
    sleep(1)
    print('~' * 30)
    print(f'\033[0;34m{"ACESSANDO O MANUAL":^30}\033[m')
    print('~' * 30)
    sleep(1)
    print()
    print(help(funcao))
    print()
    print('~' * 30)
    print(f'\033[0;32m{"SISTEMA DE AJUDA PyHELP":^30}\033[m')
    print('~' * 30)
    funcao = input('\n\033[0;34mFunção ou Biblioteca > \033[m')

print('\n\033[0;31mObrigado por utilizar nossos sistemas, Até Logo!\033[m')

