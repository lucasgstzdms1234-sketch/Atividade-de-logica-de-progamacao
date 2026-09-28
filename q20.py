import math

# 1. Entrada de dados
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# 2. Descobrir quem é o maior e quem é o menor
if num1 < num2:
    menor = num1
    maior = num2
else:
    menor = num1
    maior = num2

# 3. Calcular o quadrado do menor número
quadrado_menor = menor ** 2
print(f"O quadrado do menor número ({menor}) é: {quadrado_menor}")

# 4. Calcular a raiz quadrada do maior número (se for possível)
if maior >= 0:
    raiz_maior = math.sqrt(maior)
    print(f"A raiz quadrada do maior número ({maior}) é: {raiz_maior}")
else:
    print(f"Não é possível calcular a raiz quadrada do maior número ({maior}) porque ele é negativo.")

