from controllers.menu_login import menu_login
from controllers.menu_cadastro import cadastro_usuarios
from data.banco import carregar_usuarios

def menu():
    """Cria o menu principal"""

    #carrega a lista de usuários cadastrados
    usuarios = carregar_usuarios()

    print("*" * 40)
    print(" " * 18, "MENU", " " * 18)
    print("*" * 40)
    
    while True:
        print("\nDigite a opção desejada:")
        print("1 - Login")
        print("2 - Cadastro")
        print("0 - Sair")
        resposta = input("-> ")

        if resposta == "1":
            menu_login(usuarios)

        elif resposta == "2":
            cadastro_usuarios(usuarios)
            #atualiza a lista de usuarios cadastrados
            usuarios = carregar_usuarios()   

        elif resposta == "0":
            break

        else:
            print("Opção inválida.")