idade = int(input("Digite a sua idade: "))

if idade < 0:
    print("idade inválida")
elif idade <= 12:
    print("Você é uma criança.")
elif idade <= 17:
    print("Você é um adolescente.")
elif idade <= 59:
    print("Você é um adulto.")
else:
    print("você é im idoso")
    
print("Fim do programa")