#14. Entrar com o peso e a altura de uma determinada pessoa. Após a digitação, exibir se esta pessoa está ou não com seu peso ideal. Fórmula: peso/altura².

peso = float(input("digite seu peso em kg:"))
altura = float(input("digite sua altura em metro:"))

imc = peso / (altura * altura)

if imc < 20:
   print("abaixo do peso")
elif 20 <= imc <= 25:
   print("esta no peso ideal")

else:
   print("sobrepeso")
