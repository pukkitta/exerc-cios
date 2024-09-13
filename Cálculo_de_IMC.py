# Solicita a altura e o peso ao usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Exibe o resultado
print(f"Seu IMC é: {imc:.2f}")

# Interpreta o IMC
if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 24.9:
    print("Seu peso está normal.")
elif 25 <= imc < 29.9:
    print("Você está acima do peso.")
else:
    print("Você está com obesidade.")
