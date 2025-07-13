#23. Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C.

a = int(input("digite o valor de a: "))
b = int(input("digite o valor de b: "))
c = int(input("digite o valor de c: "))

if ((a + b) < c):
    print("a soma dos dois valores é menor que C!")
else:
    print("a soma dos dois valores é maior que C!")
    