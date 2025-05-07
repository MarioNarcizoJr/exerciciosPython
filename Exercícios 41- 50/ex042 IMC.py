peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso / altura**2

if imc < 18.5:
    print(f'Seu IMC deu {imc:.2f}, logo você está ABAIXO DO PESO, alimente-se!')
elif imc >= 18.5 and imc < 25:
    print(f'Seu IMC deu {imc:.2f}, logo você está no PESO IDEAL, parabéns!')
elif imc >= 25 and imc < 30:
    print(f'Seu IMC deu {imc:.2f}, logo você está no SOBREPESO, cuide-se!')
elif imc >= 30 and imc < 40:
    print(f'Seu IMC deu {imc:.2f}, logo você está em OBESIDADE, procure um médico!')
else:
    print(f'Seu IMC deu {imc:.2f}, logo você está em OBESIDADE MÓRBIDA, vá ao médico urgente!')
