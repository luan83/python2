import random

def ganhador(escolha_jogador, escolha_computador):
    if escolha_jogador == escolha_computador:
        return "empate"
    elif (
        (escolha_jogador == "papel" and escolha_computador == "pedra") or
        (escolha_jogador == "tesoura" and escolha_computador == "papel") or
        (escolha_jogador == "pedra" and escolha_computador == "tesoura")
    ):
        return "voce ganhou"
    else:
        return "voce perdeu"


def JogarJokenpo():
    opcoes = ["pedra", "papel", "tesoura"]
    vitorias = 0
    derrotas = 0

    print("ola, tudo bom!")
    print("ESCOLHA: pedra, papel ou tesoura")

    while True:
        escolha_jogador = input("Sua escolha:")
        if escolha_jogador not in opcoes:
            print("Escolha invalida. Tente novamente.")
            continue

        escolha_computador = random.choice(opcoes)

        print(f"computador escolheu: {escolha_computador}")

        resultado = ganhador(escolha_jogador, escolha_computador)
        print(resultado)

        if resultado == "voce ganhou":
            vitorias += 1
        elif resultado == "voce perdeu":
            derrotas += 1

        print(f"voce tem {vitorias} vitorias e {derrotas} derrotas")

        jogar_novamente = input("Você quer jogar novamente? ").lower()

        if jogar_novamente != "sim":
            break

if __name__ == "__main__":
    JogarJokenpo()