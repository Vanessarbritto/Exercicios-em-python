#16. Verificar se três valores quaisquer (A, B, C) que serão digitados formam ou não um triângulo retângulo. Lembre-se que o quadrado da hipotenusa é igual a soma dos quadrados dos catetos.

a = int(input("digite o valor do primeiro cateto: "))
b = int(input("digite o valor do segunto cateto: "))
c = int(input("digite o valor da hipotenusa: "))

if ((c * c) == (b * b) + (a * a)):
    print("E um triangulo retangulo")
else:
    print("Nao e um triangulo retangulo")
