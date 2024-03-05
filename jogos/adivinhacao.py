import random

numero = random.randint(1,10)
tentativas = 0
maxTentativas = 10

print("que comece os jogos")
print(f"voce possui {maxTentativas} tentativas")
while tentativas < maxTentativas:
    escolha = int(input("escolha um numero"))
    tentativas += 1
    if escolha == numero:
        print ("parabens voce acertou o numero")
        break
    elif escolha < numero:
        print ('Tente um valor mais alto')
    else:
        print('Tente um valor mais baixo')
    
    if tentativas == maxTentativas:
        print('Voce esgotou seu numero de tentativas')
        break
    else:
        print(f'Voce possui {maxTentativas - tentativas} tentativas')
    
print ("obrigado por jogar")