from controllers.utils import excluir_perfil

def menu_usuario(usuario_logado, usuarios):
    """Cria um menu exclusivo para usuários"""

    print(f"Você está logado como {usuario_logado.username}")

    while True:
        print("\nDigite a opção desejada:")
        print("1 - ver perfil")
        print("2 - Excluir perfil")
        print("0 - sair")   

        opcao = input("-> ")

        if opcao == "1":
            info = usuario_logado.describe_user()
            print(info)

        elif opcao == "2":
            excluir_perfil(usuario_logado, usuarios)
        
        elif opcao == "0":
            break    