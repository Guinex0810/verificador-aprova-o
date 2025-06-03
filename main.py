
# Verificador de aprovação de alunos

# Entrada de dados
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Cálculo da média
media = (nota1 + nota2) / 2

# Verificação de aprovação
if media >= 7:
    print("O aluno", nome, "foi aprovado com sucesso!")
    situacao = "Aprovado"
elif media >= 5:
    print("O aluno", nome, "está em recuperação")
    situacao = "Recuperação"
else:
    print("O aluno", nome, "foi reprovado")
    situacao = "Reprovado"

# Saída
print(f"\nAluno: {nome}")
print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")
