valores = []

for i in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {i}: ')))

maior = max(valores)
menor = min(valores)

qtd1 = valores.count(maior)
qtd2 = valores.count(menor)

print()
print(valores)
print(f'O maior número foi {maior} e está nas posições: ', end='')
for i in range(0, len(valores)):
    if valores[i] == maior:
        print(i, end=' ')
print(f'\nO menor número foi {menor} e está nas posições: ', end='')
for i in range(0, len(valores)):
    if valores[i] == menor:
        print(i, end=' ')