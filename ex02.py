a = int(input('Informe o valor de a: '))
b = int(input('Informe o valor de b: '))
c = int(input('Informe o valor de c: '))

delta = b**2 - 4 * a * c

if delta > 0:
    print("2 raizes reais")
elif delta == 0:
    print("1 raiz real")
else:
    print("não existe raiz real")