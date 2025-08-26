def calcular_desconto(valor_produto, porcentagem_desconto):
    desconto = valor_produto * (porcentagem_desconto / 100)
    valor_com_desconto = valor_produto - desconto

    return round(valor_com_desconto,2)





#codigo main
total_conta = float(input("Digite o valor total da conta: "))
porcentagem_desconto = float(input("Digite a porcentagem do desconto: "))

valor_final = calcular_desconto(total_conta, porcentagem_desconto)

print(f"O valor da gorjeta é: R${valor_final}")