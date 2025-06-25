#20. Uma escola com cursos em regime semestral realiza duas avaliações durante o semestre e calcula a média do aluno, seguinte maneira: MEDIA = (P1 + 2.P2) / 3 Fazer um programa para entrar via teclado com o valor da primeira nota (P1) e o programa deverá calcular quanto o aluno precisa tirar na segunda nota minimamente (P2) para ser aprovado, sabendo que a média de aprovação é igual cinco

nota1 = int(input("digite o valor da primeira nota:"))

resultado = (15 - (nota1 * nota1) / 3)

print(f"para ser aprovado com média 5,precisa tirar {p2_necessaria:.2f} na p2.")