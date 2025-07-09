#13. Entrar via teclado com três valores distintos. Exibir o maior deles

a = int(input("primeiro valor: "))
b = int(input("segundo valor: "))
c = int(input("terceiro valor: "))

if (a > b and a > c):
    print("O valor maior e:", a)
elif (b > a and b > c):
    print("O valor maior e:", b)
else:
     print("O maior valor é:", c)    