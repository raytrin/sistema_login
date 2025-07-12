class User:
    """Representa a estrutura básica de um usuário"""

    def __init__(self, first_name, last_name, username, password, age, email, tipo="user"):
        """Inicia os atributos para descrever o usuário"""

        self.first_name = first_name
        self.last_name = last_name 
        self.username = username
        self.password = password
        self.age = age
        self.email = email
        self.tipo = tipo


    def describe_user(self):
        """Imprime as informações dos usuários"""

        return f"""
        Nome: {self.first_name} {self.last_name}
        Idade: {self.age}
        Username: {self.username}
        E-mail: {self.email}
        """

    def greet_user(self):
        """Retorna saudação personalizada"""
        
        return f'Olá, {self.first_name}!'

    def user_data(self):
        """Converte o usuário para dicionário"""

        return {
        "first_name": self.first_name,
        "last_name": self.last_name,
        "username": self.username,
        "password": self.password.decode() if isinstance(self.password, bytes) else self.password,
        "email": self.email,
        "age": self.age,
        "tipo": self.tipo
        }


    def __str__(self):
        """Representação string do objeto"""

        return f"{self.first_name} {self.last_name} | Username: {self.username} | E-mail: {self.email}"
    

