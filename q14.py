numero1= int(input("Digite o primeiro numero:"))
numero2= int(input("Digite o segundo numero:"))
numero3= int(input("Digite o terceiro numero:"))
valores= [numero1, numero2, numero3]
valores_ordenados= sorted(valores)
print("Valores em ordem crescente:", valores_ordenados)
intermediario= valores_ordenados[1]
maior= valores_ordenados[2]
menor= valores_ordenados[0]
print("Intermediário:", intermediario)
print("Maior:", maior)
print("Menor:", menor)
