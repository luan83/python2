Nome = input ("Digite seu nome")
Idade = input ("Digite sua idade")

Idade = int (Idade)

print (f"Ola {Nome}, voce tem {Idade} anos de idade")

num1 = int (input("Escreva o primeiro valor"))
num2 = int (input("Escreva o segundo valor"))
resultado = num1 + num2
print (f"o resultado foi {resultado}")

try:
    numero = int(input("Digite um numero:"))
    print (f"O numero digitado foi {numero}.")
except ValueError:
    print ("Erro: Por favor, digite um numero valido.")