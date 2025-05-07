termo1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
pa = termo1 + 9*razao

print('-=-'*10)
print('10 TERMOS DE UMA PA')
print('-=-'*10)

for variavel in range (termo1, pa+1, razao):
    print(variavel, end=' -> ')
print('FIM')