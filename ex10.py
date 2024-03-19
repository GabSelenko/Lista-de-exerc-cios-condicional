faculdade = input("qual a sua faculdade? \n 1 - PUCPR \n 2 - UNICAMP\n")

#verifica primeiro se é uma das duas facul

if faculdade == "1":

   #pergunta as notas

    nota1 = float(input("informe a primeira nota: "))
    nota2 = float(input("informe a segunda nota: "))
    media = (nota1 + nota2)/2

    

    print("Você está na PUC!")

    #verificando medias

    if media >= 7 and media <= 10:
        print("Aprovado!!!")
    elif media >= 4 and media < 7:
        print("Recuperação final!!!")
    else:
        print("reprovado!!!")

elif faculdade == '2':
    #pergunta as notas

    nota1 = float(input("informe a primeira nota: "))
    nota2 = float(input("informe a segunda nota: "))
    media = (nota1 + nota2)/2

    print("Você está na unicamp")

    #verificando medias
    if media >= 5 and media <= 10:
        print("Aprovado")
    else:
        print("recuperação final")

else:
    print("Sua faculdade não é nem PUCPR nem UNICAMP")