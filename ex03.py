temperatura = int(input("Quantos graus está?\n "))

if temperatura <= 15:
    print('Está frio !')
elif temperatura >= 25:
    print('Está calor')
elif temperatura <= 24 and temperatura >= 16:
    print("temperatura agradavel")