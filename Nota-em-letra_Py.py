# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#  Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E

# Recebimento de valores
nota1 = float(input("Insira sua primeira nota"))
nota2 = float(input("Insira sua primeira nota"))
# Contagem de media
total_nota = nota1 + nota2
valor_final = total_nota/2
# Aqui é logica basica
if valor_final >= 9:
    print("Nota A")
elif 7.5 < valor_final < 9:
    print("Nota B")
elif 6 <= valor_final < 7.5:
    print("Nota C")
elif 4 <= valor_final < 6:
    print("Nota D")
elif valor_final < 4:
    print("Nota E")

# Ass: CrazyOreo/Pedro Macegosa;