num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} é o maior número")
elif num2 > num1 and num2 > num3:
    print(f"{num2} é o maior número")
elif num3 > num1 and num3 > num2:
    print(f"{num3} é o maior número")
elif num1 == num2 or num2 == num3 or num1 == num3:
    print(f"os números digitados são iguais.")


maior = max(num1, num2, num3):
print(f"o {maior} é o maior número")
