import bcrypt
import re

class GerenciamentoSeguranca:

    @staticmethod
    def hash_password(password):
        """Retorna hash de senha"""

        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
    @staticmethod
    def verificar_password(password, hash_password):
        """Retorna a verificação entre a senha digitada e a armazenada"""
        if isinstance(hash_password, str):
            hash_password = hash_password.encode('utf-8')

        return bcrypt.checkpw(password.encode(), hash_password)

    @staticmethod
    def email_valido(email):
        """Retorna se o email digitado é válido"""

        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    @staticmethod
    def verifica_campos_preenchidos(**campos):
        """Verifica se todos os campos foram preenchidos. 
            Retorna True se foram, e False caso contrário
        """
        for nome, valor in campos.items():
            if not valor:
                return False
        return True


