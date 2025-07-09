#28. Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem crescente

a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
c = int(input("Digite o terceiro número inteiro: "))

if a == b or a == c or b == c:
    print("Erro: os três números devem ser diferentes.")
 
else:
    if a < b and a < c:
        if b < c:
            print("Ordem crescente:", a, b, c)
        else:
            print("Ordem crescente:", a, c, b)
    elif b < a and b < c:
        if a < c:
            print("Ordem crescente:", b, a, c)
        else:
            print("Ordem crescente:", b, c, a)

    else:  # c é o menor
        if a < b:
            print("Ordem crescente:", c, a, b)
        else:
            print("Ordem crescente:", c, b, a)

