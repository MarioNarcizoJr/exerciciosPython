sexo = input('Digite seu sexo [M/F]: ')
while sexo not in 'FfMm':
    sexo = input('Fora dos parâmetros, digite novamente [M/F]: ')
print(f'Obrigado por utilizar nossos serviços, sexo {sexo} cadastrado com sucesso!')