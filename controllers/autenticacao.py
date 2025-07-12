from data.banco import salvar_usuarios
from classes.user import User
from controllers.seguranca import GerenciamentoSeguranca

class GerenciamentoAutenticacao:

    @staticmethod
    def login(usuarios, username, password): 
        """Verifica se o usuário e senha estão corretos"""
        for user in usuarios:
            if user.username == username:
                if GerenciamentoSeguranca.verificar_password(password, user.password): 
                    return user
        return None
    

    @staticmethod
    def verifica_username(usuarios, username):
        """Verifica se o username já está em uso"""
        for user in usuarios:
            if user.username == username:
                return user
        return None
    

    @staticmethod
    def verifica_email_cadastrado(usuarios, email):
        """Verifica se o email já está em uso"""

        for user in usuarios:
            if user.email == email:
                return True
        return False
      

    @staticmethod
    def cadastrar_usuario(usuarios, first_name, last_name, username, password, age, email):
        """Faz a verificação dos campos necessários pro cadastro e inclui o novo usuario no sistema"""

        if GerenciamentoAutenticacao.verifica_email_cadastrado(usuarios, email):

            return False
        
        if not GerenciamentoSeguranca.email_valido(email):

            return False
        
        if GerenciamentoAutenticacao.verifica_username(usuarios, username):

            return False
        
        if not GerenciamentoSeguranca.verifica_campos_preenchidos(
            first_name=first_name, last_name=last_name, 
            username=username, age=age, email=email, password=password
        ):
            return False

        hashed_password = GerenciamentoSeguranca.hash_password(password)

        novo_usuario = User(first_name, last_name, username, hashed_password, age, email)
        usuarios.append(novo_usuario)
        salvar_usuarios(usuarios)

        return True
    





    

    
    
            