# ================================================
# AULA 3 - CONDICIONAIS
# ================================================

# 1️⃣ Ler uma nota e verificar se é maior ou igual a 60
print("\nEXERCÍCIO 1")
nota = float(input("Digite a nota: "))

if nota >= 60:
    print("APROVADO")


# 2️⃣ Ler uma nota e mostrar se foi aprovado ou reprovado
print("\nEXERCÍCIO 2")
nota = float(input("Digite a nota: "))

if nota >= 60:
    print("APROVADO")
else:
    print("REPROVADO")


# 3️⃣ Verificar nota válida e aprovação
print("\nEXERCÍCIO 3")
nota = float(input("Digite a nota: "))

if nota < 0 or nota > 100:
    print("NOTA INVÁLIDA")
elif nota >= 60:
    print("APROVADO")
else:
    print("REPROVADO")


# 4️⃣ Verificar se o número é par ou ímpar
print("\nEXERCÍCIO 4")
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é PAR")
else:
    print("O número é ÍMPAR")


# 5️⃣ Verificar se o número termina com 0
print("\nEXERCÍCIO 5")
numero = int(input("Digite um número inteiro: "))

if numero % 10 == 0:
    print("O número termina com 0. Metade dele é:", numero / 2)
else:
    print("O número digitado não termina com 0")


# 6️⃣ Verificar se o número é positivo, negativo ou neutro
print("\nEXERCÍCIO 6")
numero = float(input("Digite um número: "))

if numero > 0:
    print("Número positivo")
elif numero < 0:
    print("Número negativo")
else:
    print("Número neutro (zero)")


# 7️⃣ Reajuste de salário conforme tempo de serviço
print("\nEXERCÍCIO 7")
salario = float(input("Digite o salário atual: R$ "))
tempo_servico = float(input("Digite o tempo de serviço (em anos): "))

if tempo_servico <= 1:
    salario_reajustado = salario * 1.10
else:
    salario_reajustado = salario * 1.20

print("Salário reajustado: R$", salario_reajustado)


# 8️⃣ Calcular idade e classificar faixa etária
print("\nEXERCÍCIO 8")
ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite o ano de nascimento: "))

idade = ano_atual - ano_nascimento
print("Idade:", idade, "anos")

if idade < 0:
    print("Ano de nascimento inválido!")
elif idade <= 3:
    print("Bebê")
elif idade <= 10:
    print("Criança")
elif idade <= 18:
    print("Adolescente")
elif idade <= 50:
    print("Adulto")
else:
    print("Idoso")


# 9️⃣ Mostrar o nome do mês por extenso
print("\nEXERCÍCIO 9")
mes = int(input("Digite o número do mês (1 a 12): "))

if mes == 1:
    print("Janeiro")
elif mes == 2:
    print("Fevereiro")
elif mes == 3:
    print("Março")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Maio")
elif mes == 6:
    print("Junho")
elif mes == 7:
    print("Julho")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Setembro")
elif mes == 10:
    print("Outubro")
elif mes == 11:
    print("Novembro")
elif mes == 12:
    print("Dezembro")
else:
    print("Mês inválido")

# ================================================
# FIM DA AULA 3
# ================================================
