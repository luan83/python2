import random
import jogos

def dificuldade():
    print("Temos 3 tipos de dificuldade além da personalizada.")
    print("Dificuldade (1) Temos que acertar um valor de 0 a 10 em 10 tentativas.")
    print("Dificuldade (2) Temos que acertar um valor de 0 a 50 em 7 tentativas.")
    print("Dificuldade (3) Temos que acertar um valor de 0 a 100 em 5 tentativas.")
    print("Dificuldade (4) Você escolhe os valores.")
    dificuldade = int(input("Digite a dificuldade que você deseja: "))
    return dificuldade

def pontuacao(tentativas):
    pontuacaoPor = 1000 / (tentativas - (tentativas / 2))
    return pontuacaoPor

dificuldade_escolhida = dificuldade()
maxTentativas = 10 if dificuldade_escolhida == 1 else 7 if dificuldade_escolhida == 2 else 5 if dificuldade_escolhida == 3 else int(input("Digite o número de tentativas desejado: "))
maxNumero = 10 if dificuldade_escolhida == 1 else 50 if dificuldade_escolhida == 2 else 100 if dificuldade_escolhida == 3 else int(input("Digite o número máximo que será sorteado: "))
tentativas = 0
pontuacaoPorTentativa = pontuacao(maxTentativas)
pontuacaoAtual = 1000

numero = random.randint(1, maxNumero)

while tentativas < maxTentativas:
    tentativas += 1
    tentativasRestantes = maxTentativas - tentativas
    pontuacaoAtual -= pontuacaoPorTentativa
    numeroEscolhido = int(input(f"Escolha um numero entre 0 e {maxNumero}: "))

    if numeroEscolhido == numero: 
        print (f"Você acertou o numero sorteado em {tentativas}")
        print (f"Sua pontuação foi de {pontuacaoAtual} Pontos.")
        break
    elif numeroEscolhido > numero:
        print (f"O numero escolhido é menor que o numero que você escolheu.")
        print (f"Você ainda tem {tentativasRestantes}")
        print (f"Sua pontuação atual é {pontuacaoAtual}") 
    elif numeroEscolhido < numero:
        print (f"O numero escolhido é maior que o numero que você escolheu.")
        print (f"Você ainda tem {tentativasRestantes}")
        print (f"Sua pontuação atual é {pontuacaoAtual}") 
    else:
        print (f"Bah guri, não deveria cair nesse else, oque você digitou ai?")
    
print (f"Infelizmente você perder, Obrigado por jogar. Tente novamente!")

if __name__ == "__name__":
    jogar_adivinha()