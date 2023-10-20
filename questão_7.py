while True:
    num = int(input("digite um número: "))
    if num < 0:
        print("Esse número é negativo. ")
    elif num > 0:
        break
 
for valores in range (num+1, 0, -1):
    print(valores)