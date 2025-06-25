#24. Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso sexo seja “F” e estado civil seja “CASADA”,solicitar o tempo de casada (anos).

nome = input("escreva seu nome:")
sexo = input("digite seu sexo (M/F):")
estado_civil = input("escreva seu estado civil:")

if sexo == "F" and estado_civil == "CASADA":
    tempo_casada = input("quantos anos de casamento?")
    print(f"{nome},voce esta casada ha {tempo_casada} anos.")

else:
    print(f"{nome}, obrigado pelas informacoes.")