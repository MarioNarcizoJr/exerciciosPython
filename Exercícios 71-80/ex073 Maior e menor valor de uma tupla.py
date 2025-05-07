from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(numeros)
print(f'O maior valor foi {max(numeros)} e o menor foi {min(numeros)}')

#from random import sample
#a = tuple(sample(range(10), 5))
#print(a)
#print(f'O maior valor é {max(a)} e o menor é {min(a)}.')