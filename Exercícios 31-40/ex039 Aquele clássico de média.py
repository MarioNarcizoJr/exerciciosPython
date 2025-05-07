nota1 = float(input('Digite quanto você tirou na primeira avaliação: '))
nota2 = float(input('Digite quanto você tirou na segunda avaliação: '))
media = (nota1 + nota2)/2
if media < 5:
    print(f'Com as notas {nota1} e {nota2}, sua média é {media}. Infelizmente você está REPROVADO.')
elif media >= 7:
    print(f'Com as notas {nota1} e {nota2}, sua média é {media}. Parabéns você está APROVADO')
else:
    print(f'Com as notas {nota1}e {nota2}, sua média é {media}. Você está de RECUPERAÇÃO.')