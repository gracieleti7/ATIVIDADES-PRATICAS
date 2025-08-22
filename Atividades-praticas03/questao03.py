temperatura = float(input("Digite a temperatura em: "))

unidadeOrigem = input("Digite a unidade de origem (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper()
unidadeDestino = input("Digite a unidade de destino (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper()

if unidadeOrigem == 'C':
    if unidadeDestino == 'F':
        temperaturaConvertida = (temperatura * 9/5) + 32
    elif unidadeDestino == 'K':
        temperaturaConvertida = temperatura + 273.15
    else:
        temperaturaConvertida = temperatura
elif unidadeOrigem == 'F':
    if unidadeDestino == 'C':
        temperaturaConvertida = (temperatura - 32) * 5/9
    elif unidadeDestino == 'K':
        temperaturaConvertida = (temperatura - 32) * 5/9 + 273.15
    else:
        temperaturaConvertida = temperatura
elif unidadeOrigem == 'K':
    if unidadeDestino == 'C':
        temperaturaConvertida = temperatura - 273.15
    elif unidadeDestino == 'F':
        temperaturaConvertida = (temperatura - 273.15) * 9/5 + 32
    else:
        temperaturaConvertida = temperatura
else:
    print("Unidade de origem inválida.")
    temperaturaConvertida = None

print(f"\nTemperatura convertida: {temperaturaConvertida:.2f} {unidadeDestino}") if temperaturaConvertida is not None else None