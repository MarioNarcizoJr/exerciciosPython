import random
from time import sleep
print('''====== Pedra Papel Tesoura ======
[1] Pedra 
[2] Papel
[3] Tesoura
Tente me vencer Hahaha
''')
opcao = int(input('Digite sua opção: '))
aleatorio = random.randint(1, 3)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

if opcao < 1 or opcao > 3:
    print('Opção fora dos parâmetros, tente novamente.')
elif opcao == 1 and aleatorio == 3:
    print('Parabéns você ganhou, você jogou Pedra e o computador escolheu tesoura.')
elif opcao == 2 and aleatorio == 1:
    print('Parabéns você ganhou, você jogou Papel e o computador escolheu pedra.')
elif opcao == 3 and aleatorio == 2:
    print('Parabéns você ganhou, você jogou Tesoura e o computador escolheu papel.')
elif aleatorio == 1 and opcao == 3:
    print('Perdeu, o computador escolheu Pedra e você tesoura.')
elif aleatorio == 2 and opcao == 1:
    print('Perdeu, o computador escolheu Papel e você escolheu pedra.')
else:
    print('Perdeu, o computador escolheu Tesoura e você escolheu papel.')
