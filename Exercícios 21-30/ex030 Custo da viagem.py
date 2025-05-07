distancia = int(input('Digite a distância em km da viagem: '))
if distancia <= 200:
    print(f'A sua viagem é de {distancia}km, custará R${(distancia*0.5):.2f} reais.')
elif distancia < 0:
    print('Distância negativa, não existe.')
else:
    print(f'A sua viagem é maior que 200km, custará R${(distancia*0.45):.2f} reais.')
