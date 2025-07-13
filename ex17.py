#17- Entrar com o peso, o sexo e a altura de uma determinada
#pessoa. Após a digitação, exibir se esta pessoa está ou não
#com seu peso ideal. Fórmula: peso/altura². */

peso = float(input(" digite seu peso: "))
altura = float(input("digite sua altura: "))
sexo = input("insira seu sexo (F/M): ")

imc = peso / (altura * altura)

if (sexo == "M" or "m"):
   if (imc <20):
        print("abaixo do peso")
   elif (imc <25):
        print("peso ideal")
   else:
        print("acima do peso")
elif (sexo == "F"or "f"):
   if (imc < 18):
       print("abaixo do peso") 
   elif (imc < 24):
       print("peso ideal")
   else:
       print("acima do peso")
