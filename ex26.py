#26. Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, imprimindo o resultado.

numero = float(input("Digite um número: "))

if numero >= 0:
    resultado = numero * 2
    print("O número é positivo. O dobro é:", resultado)
else:
    resultado = numero * 3
    print("O número é negativo. O triplo é:", resultado)
