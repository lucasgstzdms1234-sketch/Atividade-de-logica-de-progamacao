numero= int(input("Digite um numero:"))
if numero == 5 or numero == 200 or numero == 400:
    print("O numero digitado é igual a 5, 200 e 400")
elif numero > 500 and numero < 1000:
    print("O numero digitado está entre 500 e 1000")
else:
    print("O numero digitado não atende a nenhuma das condições")