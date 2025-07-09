#29. Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem decrescente.

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a == b or a == c or b == c:
       print("os tres numeros devem ser diferentes");
else:
    if a > b and a > c:
        if b > c:
            print(c, b, a)
        else:
            print(b, c, a)
    elif b > a and b > c:
        if a > c:
            print(c, a, b)
        else:
            print(a, c, b)
    else:
        if a > b:
            print(b, a, c)
        else:
            print(a, b, c)