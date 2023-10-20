frase = str(input("digite uma frase: "))
contadorV = 0
contadorC = 0
for letra in frase:
    if letra in "aeiou":
       contadorV +=1
for letra in frase:
    if letra in "bcdfghjklmnpqrstvwxyz":
        contadorC +=1
print(f"a frase '{frase}' tem {contadorV} vogais e {contadorC} consoantes ")