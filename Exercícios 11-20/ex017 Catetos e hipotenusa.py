catoposto = float(input('Digite a medida do cateto oposto: '))
catadjacente = float(input('Digite a medida do cateto adjacente: '))
print(f'Com a medida {catoposto} do cateto oposto e {catadjacente} do cateto adjacente, a hipotenusa vale {((catoposto**2 + catadjacente**2)**0.5):.2f}.')
#Ou chamar o método Hypo da biblioteca math.Hypot(catoposto, catadjacente)
