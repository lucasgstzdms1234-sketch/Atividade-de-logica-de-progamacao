numero1= int(input("Digite o primeiro numero:"))
numero2= int(input("Digite o segundo numero:"))
numero3= int(input("Digite o terceiro numero:"))
valores= [numero1, numero2, numero3]
valores_ordenados= sorted(valores, reverse=True)
print("Valores em ordem decrescente:", valores_ordenados)
