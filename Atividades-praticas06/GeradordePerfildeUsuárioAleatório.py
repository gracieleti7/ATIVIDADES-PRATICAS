import requests

def obter_usuario_aleatorio():
    url = "https://randomuser.me/api/"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()['results'][0]
        nome = f"{dados['name']['first']} {dados['name']['last']}"
        email = dados['email']
        pais = dados['location']['country']
        return f"""
            Nome: {nome}
            Email: {email}
            País: {pais}
        """
    except requests.RequestsException as e:
        print(f"Erro ao obter usuário aleatório: {e}")
        return None
    
print("Obtendo usuário aleatório...")
usuario = obter_usuario_aleatorio()
print(usuario)