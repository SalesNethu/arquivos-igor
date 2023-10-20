num1 = float(input("digite o número: ")) 
num2 = float(input("digite o número: "))
operation = str(input("""
Qual operação você deseja realizar? 
S - Soma
SUB - Subtração
D - Divisão
M - Multiplicação
""")).upper()



if operation == "S":
        resultado = num1 + num2 
        if resultado % 2 == 0:
            print(f"{resultado} é par")
        elif resultado % 2 != 0:
            print(f"{resultado} é ímpar")
        if resultado > 0:
            print(f"{resultado} é positivo")
        elif resultado < 0:
            print(f"{resultado} é negativo.")

if operation == "SUB":
        resultado = num1 - num2 
        if resultado % 2 == 0:
            print(f"{resultado} é par")
        elif resultado % 2 != 0:
            print(f"{resultado} é ímpar")
        if resultado > 0:
            print(f"{resultado} é positivo")
        elif resultado < 0:
            print(f"{resultado} é negativo.")


if operation == "M":
        resultado = num1 * num2 
        if resultado % 2 == 0:
            print(f"{resultado} é par")
        elif resultado % 2 != 0:
            print(f"{resultado} é ímpar")
        if resultado > 0:
            print(f"{resultado} é positivo")
        elif resultado < 0:
            print(f"{resultado} é negativo.")
    

if operation == "D":
        resultado = num1 / num2 
        if resultado % 2 == 0:
            print(f"{resultado} é par")
        elif resultado % 2 != 0:
            print(f"{resultado} é ímpar")
        if resultado > 0:
            print(f"{resultado} é positivo")
        elif resultado < 0:
            print(f"{resultado} é negativo.")
