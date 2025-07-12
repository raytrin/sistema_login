from getpass import getpass
from controllers.autenticacao import GerenciamentoAutenticacao

def cadastro_usuarios(usuarios):
    """Recebe as informações do usuário e adiciona à lista de usuários caso elas ainda não tenham sido gravadas """


    print("\n---- Cadastro de usuário ----\n")
    
    first_name = input("\nNome: ").strip()
    last_name = input("Sobrenome: ").strip()
    username = input("Username: ").strip()
    password = getpass("Senha: ")

    while True:
        try:
            age = int(input("Idade: "))
            break   
        except ValueError:
            print("Digite um número válido para a idade.")

    email = input("E-mail: ")

    #verifica se os dados preenchidos satisfazem as necessidades pro cadastro bem-sucedido
    if not GerenciamentoAutenticacao.cadastrar_usuario(usuarios, first_name, last_name, username, password, age, email):
        print("Não foi possível realizar o cadastro. Verifique as informações.")
