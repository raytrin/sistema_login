import json
from classes.user import User


arquivo_usuarios = "usuarios.json"

def carregar_usuarios():
    """Abre o arquivo json, carrega os usuarios pra lista usuários e retorna a lista"""

    try:
        with open(arquivo_usuarios, "r", encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

            usuarios = []
            for user_dados in dados:
                usuarios.append(User(**user_dados))

            return usuarios
    except FileNotFoundError:
        return []
    
def salvar_usuarios(usuarios):
    """Salva os usuários da lista no arquivo json"""
    
    dados = []
    for user in usuarios:
        dados.append(user.user_data())

    with open(arquivo_usuarios, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)