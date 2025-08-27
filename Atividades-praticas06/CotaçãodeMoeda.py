import requests

def obter_cotacao_atual(moeda):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()[f"{moeda}BRL"]
        return f"""
                Cotação de {moeda} para BRL:
                Valor: R$ {float(dados['bid']):.2f}
                Máxima: R$ {float(dados['high']):.2f}
                Mínima: R$ {float(dados['low']):.2f}
                Data/hora: {dados['create_date']}
                """
    except requests.RequestException as e:
        return f"Erro ao obter a cotação: {e}"
    
moeda = input("Digite o código da moeda para cotação (EUR, USD, GBP)")
resultado = obter_cotacao_atual(moeda)
print(resultado)