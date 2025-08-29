# Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.
import csv

def escrever_dados_csv(nome_arquivo, dados):
    try:
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            # Escreve o cabeçalho
            escritor_csv.writerow(['Nome', 'Idade', 'Cidade'])
            # Escreve os dados
            for linha in dados:
                escritor_csv.writerow(linha)
            return (f"Dados escritos com sucesso em {nome_arquivo}")
    except Exception as e:
        return (f"Erro ao escrever no arquivo: {e}")
    
# Exemplo de uso
dados_pessoas = [
    ['Maria', 40, 'São Paulo'],
    ['Tiago', 24, 'Rio de Janeiro'],
    ['Carlos', 28, 'Belo Horizonte'],
    ['Bruno', 35, 'Curitiba'],
    ['Julia', 21, 'Porto Alegre'],
    ['Pedro', 25, 'Salvador']
]

nome_arquivo = input("Digite o nome do arquivo CSV (ex: pessoas.csv): ")
print(escrever_dados_csv(nome_arquivo, dados_pessoas))