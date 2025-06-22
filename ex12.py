#12. Calcular e exibir a área de um retângulo, a partir dos valores da base e altura que serão digitados. Se a área for maior que 100, exibir a mensagem “Terreno grande”, caso contrário, exibir a mensagem “Terreno pequeno”.

area=0

base = int(input("digite o valor da base:"))
altura = int(input("digite o valor das altura:"))

area = base * altura

if area > 100:
   print("terreno grande")
else:
   print("terreno pequeno")