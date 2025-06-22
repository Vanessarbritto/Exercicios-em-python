1#4. Entrar com o peso e a altura de uma determinada pessoa. Após a digitação, exibir se esta pessoa está ou não com seu peso ideal. Fórmula: peso/altura².

peso = float(input("digite seu peso:"))
altura = float(input("digite sua altura:"))

imc = peso / (altura * altura)

if imc < 20:
   print("abaixo do peso")
elif 20 <= imc <= 25:
   print("esta no peso ideal")

elif 25 <= imc <= 80:
   print("sobrepeso")
