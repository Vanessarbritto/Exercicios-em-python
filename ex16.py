#16. Verificar se três valores quaisquer (A, B, C) que serão digitados formam ou não um triângulo retângulo. Lembre-se que o quadrado da hipotenusa é igual a soma dos quadrados dos catetos.

A = int(input("digite o valor do primeiro cateto:"))
B = int(input("digite o valor do segunto cateto:"))
C = int(input("digite o valor da hipotenusa"))

if ((C * C) == (B * B) + (A * A)):
    print("E um triangulo retangulo")

else:
    print("Nao e um triangulo retangulo")