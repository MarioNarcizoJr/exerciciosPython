from Pacotes.UtilidadesCeV import Dados
from Pacotes.UtilidadesCeV import Moeda

numero = Dados.leiadinheiro('Digite o preço: R$')
Moeda.resumo(numero, 10, 5)