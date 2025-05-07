alunos = []
auxiliar = []

condicao = 's'

while condicao != 'n':
    auxiliar.append(input('Nome: '))
    auxiliar.append(float(input('Nota 1: ')))
    auxiliar.append(float(input('Nota 2: ')))
    alunos.append(auxiliar[:])
    auxiliar.clear()
    condicao = input('Deseja continuar? [S/N] ').lower()

print()
print('-' * 50)
print(f'{"No.":<4} {"Nome":<10} {"MÉDIA":>8}')
print('-' * 50)


for i in range(0, len(alunos)):
    print(f'{i:<4} {alunos[i][0]:<10} {(alunos[i][1] + alunos[i][2]) / 2:>8}')

print('-' * 50)

condicao2 = int(input('\nMostrar notas de qual aluno? [999 interrompe]: '))

while condicao2 != 999:
    print(f'\nAs notas de {alunos[condicao2][0]} são {alunos[condicao2][1]} e {alunos[condicao2][2]}')
    condicao2 = int(input('\nMostrar notas de qual aluno? [999 interrompe]: '))

print('\nFinalizando...\nObrigado por utilizar nossos serviços!')
