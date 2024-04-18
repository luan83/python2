num1 = float(input("digite o primeiro numero: "))
num2 = float(input("digite o segundo numero: "))

operacao = input("escolha sua equacao +,-,*,/ : ")


def soma(num1,num2):
    resultado = num1 + num2
    print(f"Resultado é {resultado}")

def sub(num1,num2):
    resultado = num1 - num2
    print(f"Resultado é {resultado}")
    
def mult(num1,num2):
    resultado = num1 * num2
    print(f"Resultado é {resultado}")

def div(num1,num2):
    resultado = num1 / num2
    print(f"Resultado é {resultado}")

if operacao == '+':
    soma(num1,num2)
elif operacao == '-':
    sub(num1,num2)
elif operacao == '*':
    mult(num1,num2)
elif operacao == '/':
    div(num1,num2)
    
    if num2 == 0:
        resultado = "nao é possivel dividir por 0"

    else:
        resultado = num1 / num2

else:
    resultado = "operacao invalida"
    print("mostrar resultado:", resultado)
