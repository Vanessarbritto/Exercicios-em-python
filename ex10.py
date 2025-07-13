#10. Entrar com dois valores quaisquer. Exibir o maior deles, se existir, caso contrário, enviar mensagem avisando que os números são idênticos.

a = int(input("primeiro valor: "))
b = int(input("segundo valor: "))

if (a > b):
    print("o primeiro valor é maior")
elif (b > a):
    print("O segundo valor é menor")
else:
    print("Os valores são iguais!")
