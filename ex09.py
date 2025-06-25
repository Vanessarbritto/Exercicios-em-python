 #9-Entrar via teclado, com dois valores distintos. Exibir o menor deles.

a = int(input("primeiro valor: "))
b = int(input("segundo valor: "))

if a < b:
    print("O primeiro valor é menor:")
elif b < a:
    print("O segundo valor é menor:")

