from Pacotes.Interface import *
from Pacotes.Arquivos import *
from time import sleep

arquivo = 'dados.txt'

if not abrirArquivo(arquivo):
    criarArquivo(arquivo)

while True:
    print()
    resposta = menu(['\033[0;34mMostrar Todos os Usuários\033[m', '\033[0;34mCadastrar Novo Usuário\033[m', '\033[0;34mSair do Programa\033[m'])
    if resposta == 1:
        sleep(1)
        lerArquivo(arquivo)
    elif resposta == 2:
        sleep(1)
        nome = input('\nNome: ')
        idade = LeiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        sleep(1)
        print('\n\033[0;32mSaindo do programa, obrigado por utilizar nossos serviços.\033[m')
        break
    else:
        print('\033[0;31mERRO, Tente novamente!\033[m')
    sleep(2)

