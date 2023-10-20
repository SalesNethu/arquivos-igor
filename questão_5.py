grade1 = float(input("Digite a nota do aluno: "))
grade2 = float(input("Digite a nota do aluno: "))
grade3 = float(input("Digite a nota do aluno: "))
grade4 = float(input("Digite a nota do aluno: "))
media = (grade1 + grade2 + grade3 + grade4) / 4

if media == 10:
    print("Aprovado com distinção")
elif media >= 7 and media < 10:
    print("Aprovado")
else:
    print("Reprovado")
    
