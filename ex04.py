nota = float(input("informe sua nota: "))

if nota >= 7:
    print("esta aprovado!")
elif nota >= 4 and nota < 7:
    print("estudante em recuperacao")
else:
    print("reprovado")