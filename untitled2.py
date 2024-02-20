# Solicita a nota do usuário
nota = int(input("Digite sua nota: "))
# Categoriza a nota
if nota < 60:
    categoria = "F"
elif nota < 70:
    categoria = "D"
elif nota < 80:
    categoria = "C"
elif nota < 90:
    categoria = "A"
elif nota < 100:
    categoria = "A+"
elif nota == 100:
    categoria = "S"
elif nota < 988:
    categoria = "LOL"
elif nota < 999:
    categoria = "League of Legends"
elif nota <99999:
    categoria = "Dota"
print(f"Você está na categoria: {categoria}.")