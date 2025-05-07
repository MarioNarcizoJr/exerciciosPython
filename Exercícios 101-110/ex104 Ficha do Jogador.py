def jogador(nome='<Desconhecido>', x=0):
    return f'O jogador {nome} fez {x} gols no campeonato.'


atleta = input('Nome do jogador: ')
gols = int(input(f'Quantidade de gols: '))

print(jogador(atleta, gols))
print(jogador())
