import random
import time
aleatorio = random.randint(0, 5)
print('-='*29)
print('Estou pensando em um número entre 0 e 5, tente advinha-lo')
print('-='*29)
numero = int(input('Digite um número entre 0 e 5: '))
print('Processando.......')
time.sleep(2)
if numero > 5 or numero < 0:
    print('Erro, seu número está fora dos parâmetros, reinicie o programa.')
elif numero == aleatorio:
    print('GANHOU. Parabéns! Seu Qi é mais de 8000, te subestimei terráqueo.')
elif numero != aleatorio:
    print(f'PERDEU. Numéro errado, eu escolhi {aleatorio} e você {numero}. tente novamente HAHA!')