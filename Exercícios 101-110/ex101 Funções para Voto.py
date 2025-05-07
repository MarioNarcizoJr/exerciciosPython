import datetime


def voto(x):
    """
    Função Para Identificar Quem tem direito a voto:
    :param x: Idade do indivíduo
    :return: Obrigatório, Negado ou Opcional
    Função Criada por Mário Narcizo 13/07/2021
    """
    ano = datetime.date.today().year
    idade_voto = ano - x
    if idade_voto < 16:
        return f'Você tem {idade_voto} anos. Direito Negado!'
    elif 18 <= idade_voto < 70:
        return f'Você tem {idade_voto} anos. Voto OBRIGATÓRIO!'
    else:
        return f'Você tem {idade_voto} anos. Direito Opcional!'


idade = int(input('Digite o ano de seu nascimento: '))
print()
print(voto(idade))
