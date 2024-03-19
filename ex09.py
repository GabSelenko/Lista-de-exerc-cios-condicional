idade = int(input("informe sua idade: "))
tempoServiço = int(input("informe o tempo de serviço: "))

#Verificar aposentadoria

if idade >= 65:
    print("pode se aposentar")
elif tempoServiço >= 30:
    print("pode se aposentar")
elif idade >= 60 and tempoServiço >= 25:
    print("pode se aposentar")
else:
    print("não pode se aposentar")