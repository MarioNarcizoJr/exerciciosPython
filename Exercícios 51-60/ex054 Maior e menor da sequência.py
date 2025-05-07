peso = float(input('Digite o peso da 1º pessoa em kg: '))
maior = peso
menor = peso
for pessoa in range (2, 6):
    peso = float(input(f'Digite o peso da {pessoa}º pessoa em kg: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print(f'\nO maior peso registrado foi {maior}kg e o menor foi {menor}kg.')
