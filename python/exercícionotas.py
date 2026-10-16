alunos = int(input("Digite o número de alunos na turma: "))

while alunos <= 0:
    print("Valor inválido! Tente novamente.")
    alunos = int(input("Digite o número de alunos na turma: "))

notas = []

for i in range(alunos):

    nota = float(input(f"Digite a nota do aluno {i+1}: "))

    while nota < 0 or nota > 10:
        print("Valor inválido! Tente novamente.")
        nota = float(input("Digite a nota do aluno: "))

    notas.append(nota)

maior_nota = max(notas)
menor_nota = min(notas)
media = sum(notas) / alunos

aprovados = 0
reprovados = 0

for nota in notas:

    if nota >= 6:
        aprovados += 1
    else:
        reprovados += 1

print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")
print(f"Média das notas: {media}")
print(f"Número de alunos aprovados: {aprovados}")
print(f"Número de alunos reprovados: {reprovados}")