#29. Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem decrescente.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 < num2:
    num1, num2 = num2, num1
if num1 < num3:
    num1, num3 = num3, num1
if num2 < num3:
    num2, num3 = num3, num2