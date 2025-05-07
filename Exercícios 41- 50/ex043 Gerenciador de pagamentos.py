valor = float(input('Digite o valor da sua compra: R$'))
parcelas = 0
print('''\n========== LOJAS PENEDENSES ==========
Volte sempre! Formas de pagamentos:
[1] Á vista Dinheiro/Cheque
[2] Débito no cartão
[3] Crédito 2x no cartão
[4] Crédito 3x ou mais no cartão
========== LOJAS PENEDENSES ==========''')
opcao = int(input('\nDigite sua opção: '))
if opcao >= 1 or opcao <= 4:
    if opcao == 1:
        print(f'Pagamento Á VISTA com 10% de desconto, de R${valor} passa a ser R${valor - (valor * 0.1):.2f}.')
    elif opcao == 2:
        print(f'Pagamento no débito com 5% de desconto, de R${valor} passa a ser R${valor - (valor) * 0.05:.2f}.')
    elif opcao == 3:
        print(f'Pagamento no cartão parcelado para 2x, de R${valor} passa a ser 2 parcelas de R${valor/2:.2f}.')
    else:
        parcelas = int(input('Digite quantas parcelas você deseja para a compra: '))
        print(f'Pagamento no cartão parcelado para {parcelas}x, de R${valor} passa a ser {parcelas} parcelas de R${valor/parcelas + (valor/parcelas*0.2):.2f} com juros.')
else:
    print('Opção fora dos parâmetros, digite novamente a opção!')
