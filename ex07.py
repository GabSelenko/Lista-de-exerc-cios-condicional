idade = int(input("informe sua idade: "))

if idade < 14:
    print("Você não pode ir no brinquedo\n")
elif idade <= 15:
    print("Você tem idade suficiente para usar o brinquedo!!")

    peso = int(input("Informe seu peso em kg: "))

    if peso < 120:
        print('você pode ir no brinquedo')
    else:
        print("você não pode ir no brinquedo")