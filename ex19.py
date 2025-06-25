#19. Uma escola com cursos em regime semestral, realiza duas avaliações durante o semestre e calcula a média do aluno, da seguinte maneira: MEDIA = (P1 + 2.P2) / Fazer um programa para entrar via teclado com os valores das  notas (P1 e P2) e calcular a média. Exibir a situação final do aluno (“Aprovado ou Reprovado”), sabendo que a média de aprovação é igual a cinco.

nota1 = int(input("digite a primeira nota:"))
nota2 = int(input("digite a segubnda nota:"))

media = (nota1 + (nota2 * nota2) / 3)

if media >= 5:
    print ("voce esta aprovado")

else:
     media <=4
     print("voce nao foi aprovado")