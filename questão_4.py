letra = str(input("digiete qualquer letra: "))
if letra in "aeiouAEIOU":
    print(f"{letra} é Vogal.")
elif letra in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
    print(f"{letra} é consoante.")
else:
    print("caractere inválido")

