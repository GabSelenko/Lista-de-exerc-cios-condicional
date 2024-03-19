sexo = int(input("Digite seu sexo: (1 - Feminino ou 2 - Masculino)"))
altura = float(input("Digite sua altura: "))
if sexo == 1:
    print ("Feminino")
    print (f"O peso ideal e de {62.1 * altura - 44.7 :.2f}")
else: 
    print ("Masculino")
    print (f"O peso ideal e de {72.7 * altura - 58 :.2f}")