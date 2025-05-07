matriz = []

for i in range(0, 9):
    matriz.append(int(input('Digite um número: ')))

print()
print(f'''[ {matriz[0]:^2} ]  [ {matriz[1]:^2} ]  [ {matriz[2]:^2} ]
[ {matriz[3]:^2} ]  [ {matriz[4]:^2} ]  [ {matriz[5]:^2} ]
[ {matriz[6]:^2} ]  [ {matriz[7]:^2} ]  [ {matriz[8]:^2} ]''')
