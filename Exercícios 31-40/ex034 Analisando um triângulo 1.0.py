reta1 = float(input('Digite o tamanho da primeira reta: '))
reta2 = float(input('Digite o tamanho da segunda reta: '))
reta3 = float(input('Digite o tamanho da terceira reta: '))

print('-='*14)
print('Analisando as retas.........')
print('-='*14)

if reta1 < reta3 + reta2 and reta2 < reta3 + reta1 and reta3 < reta1 + reta2:
    print('Com essas três retas, é possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo com essas retas.')