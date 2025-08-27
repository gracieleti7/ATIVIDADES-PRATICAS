import requests

def consultar_cep(cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    dados = response.json()
    logradouro = dados['logradouro']
    bairro = dados['bairro']
    cidade = dados['localidade']
    estado = dados['uf']
    return logradouro, bairro, cidade, estado

cep = input("Informe o CEP: ")
logradouro, bairro, cidade, estado = consultar_cep(cep)
print("Logradouro:", logradouro)
print("Bairro:", bairro)
print("Cidade:", cidade)
print("Estado:", estado)