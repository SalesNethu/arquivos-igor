# sex = str(input("Qual seu sexo? "))
# if sex in "Ff":
#     print("Feminino")
# if sex in "Mm":
#     print("masculino")
# else:
#     print("sexo inválido")


sex = str(input("""
Digite seu sexo:
F - Feminino
M - Masculino
""")).upper()

if sex == "F":
    print("Feminino")
if sex == "M":
    print("masculino")
else:
    print("sexo inválido")