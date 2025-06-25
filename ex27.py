#27. Faça um algoritmo que leia uma variável e some 5 caso seja par ou some 8 caso seja ímpar, imprimir o resultado desta operação.

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    resultado = numero + 5
    print(f"O número é par. Após somar 5, o resultado é: {resultado}")
else:
    resultado = numero + 8
    print(f"O número é ímpar. Após somar 8, o resultado é: {resultado}")