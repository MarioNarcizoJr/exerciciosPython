def notas(*num, sit=False):
    """
    Função que recebe n notas e informa as principais informações sobre o aluno:
    :param num: N numero de notas que o código receberá
    :param sit: Variável booleana que indica a situação final do aluno
    :return: Retorna um dicionário com todas as informações
    Criado por Mário Narcizo 24/07
    """
    aluno = dict()
    aluno['qtd'] = len(num)
    aluno['maior'] = max(num)
    aluno['menor'] = min(num)
    aluno['media'] = (sum(num)/aluno["qtd"])
    if sit:
        if aluno['media'] >= 8:
            aluno['situação'] = 'Otimo, Parabéns!'
        elif aluno['media'] < 6:
            aluno['situação'] = 'Reprovado'
        elif aluno['media'] >= 6:
            aluno['situação'] = 'Boa'

    return aluno

resp = notas(10, 0, 2, 5, 9, sit=True)
print(resp)
