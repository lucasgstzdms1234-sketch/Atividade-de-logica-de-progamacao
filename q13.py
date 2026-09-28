numero1= int(input("Digite o primeiro numero:"))
numero2= int(input("Digite o segundo numero:"))
numero3= int(input("Digite o terceiro numero:"))
numero4= int(input("Digite o quarto numero:"))
if numero1 > numero2 and numero1 > numero3 and numero1 > numero4:
    print("O primeiro numero é o maior")
elif numero2 > numero1 and numero2 > numero3 and numero2 > numero4:
    print("O segundo numero é o maior")
elif numero3 > numero1 and numero3 > numero2 and numero3 > numero4:
    print("O terceiro numero é o maior")
else:
    print("O quarto numero é o maior")