distancia = float(input('Digite a distância percorrida em metros: '))
print(f'O valor de {distancia}m em: \nMilímetro é {distancia * 1000}mm\nCentímetro {distancia*100}\n'
      f'Decímetros {distancia * 10}\nDecâmetro {distancia / 10}\nHectômetro {distancia / 100}\n'
      f'Quilômetros {distancia / 1000}')
