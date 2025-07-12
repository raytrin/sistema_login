from getpass import getpass
from controllers.autenticacao import GerenciamentoAutenticacao
from controllers.menu_usuarios import menu_usuario


def menu_login(usuarios):
    """Cria a função de fazer login com username e password. Esconde a senha no terminal."""

    username = input("\nUsuário: ")
    password = getpass("Senha: ") 
    
    #Verifica se as informações estão corretas pra realizar o login
    user_logado = GerenciamentoAutenticacao.login(usuarios, username, password)

    if user_logado:
        #Saudação inicial para o usuário logado
        mensagem = user_logado.greet_user()
        print(mensagem)

        #Exibe o menu
        menu_usuario(user_logado, usuarios)

        
