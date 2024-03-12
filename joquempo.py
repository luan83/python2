import random

def JogarJokenpo():
    opcoes = ["pedra", "papel","tesoura"]
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

        print(f"Computador escolheu: {escolha_computador}")

        if escolha_jogador == escolha_computador:
            print("Empate")
        elif(
            (escolha_jogador == "papel" and escolha_computador == "pedra") or
            (escolha_jogador == "tesoura" and escolha_computador == "papel") or
            (escolha_jogador == "pedra" and escolha_computador == "tesoura")
        ):
            vitorias += 1
            print("voce ganhou")
        else:
            derrotas += 1
            print("voce perdeu!!! baka")
        print(f"voce tem {vitorias} vitorias e {derrotas} derrotas")
        jogar_novamente = input("Vocẽ quer jogar novamente?").lower()

        if jogar_novamente != "sim":
            break

if __name__ == "__main__":
    JogarJokenpo()