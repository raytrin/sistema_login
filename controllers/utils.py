from data.banco import salvar_usuarios


def buscar_usuario_por_username(usuarios): 
    """Verifica se o usuario está cadastrado. Caso esteja, retorna uma descrição dele. Caso nao, imprime uma mensagem de não encontrado e retorna None"""

    username = input("\nDigite o username: ")

    for user in usuarios:
        if user.username == username:
            user.describe_user()
            return user
    print("Usuário não encontrado.")
    return None



def excluir_perfil(usuario_logado, usuarios):
    """Exclui o perfil do usuário logado"""

    confirma_exclusao = input(f"\nConfirma a exclusão do usuário {usuario_logado.username} (s/n)? ").lower().strip()

    if confirma_exclusao == "s": 
        usuarios.remove(usuario_logado)
        salvar_usuarios(usuarios) 
        print("\nPerfil excluído com sucesso!")
                  
    elif confirma_exclusao == "n":
        print("Exclusão cancelada!")

    else:
        print("\nDigite uma opção válida!")



   

    