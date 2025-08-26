def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)

    return round(gorjeta,2)





#codigo main
total_conta = float(input("Digite o valor total da conta: "))
porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta: "))

gorjeta = calcular_gorjeta(total_conta, porcentagem_gorjeta)

print(f"O valor da gorjeta é: R${gorjeta}")