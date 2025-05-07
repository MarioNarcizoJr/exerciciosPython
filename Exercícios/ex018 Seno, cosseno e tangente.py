import math
angulo = float(input('Digite o ângulo que deseja calcular: '))
print(f'O seno do angulo de {angulo}º é {math.sin(math.radians(angulo)):.2f}\nO cosseno de {angulo}º é {math.cos(math.radians(angulo)):.2f}\n E a tangente de {angulo}º é {math.tan(math.radians(angulo)):.2f}.')
