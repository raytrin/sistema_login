# 🔐 Sistema de Autenticação em Python (terminal)

Este é um projeto simples de sistema de login e cadastro feito em Python, totalmente funcional no terminal. Ele é a base para um futuro sistema web com Flask e banco de dados.

---

## Demonstração

Ao iniciar o programa você verá o menu principal:

```
*************** MENU ***************
Digite a opção desejada:
1 - Login
2 - Cadastro
0 - Sair

```

- **Login**: escolha 1 para realizar login usando usuário e senha
- **Cadastro**: escolha 2 para realizar o cadastro usando nome, sobrenome, usuário, email e idade.
- **Sair**: escolha 0 para sair do sistema

---

## 🚀 Como Executar

1. **Clone o repositório**:
```bash
git clone https://github.com/raytrin/sistema_login.git
cd sistema_login
```

2. **Instale as dependências**:
```bash
pip install bcrypt
```

3. **Execute o programa**:
```bash
python main.py
```
---

## 📁 Estrutura
```

├── main.py                      # Arquivo principal que inicia o programa (chama o menu principal)
├── classes
│   └── user.py                  # Classe User que representa os usuários e seus dados
├── controllers
│   ├── autenticacao.py          # Lógica de cadastro, login e verificação de usuários
│   ├── menu_cadastro.py         # Interface de terminal para cadastro de novos usuários
│   ├── menu_login.py            # Interface de terminal para login de usuários
│   ├── menu_principal.py        # Menu inicial com opções de login, cadastro ou sair
│   ├── menu_usuarios.py         # Menu mostrado após login com opção de ver/excluir perfil
│   ├── seguranca.py             # Funções de segurança: hash de senha, validações, etc.
│   └── utils.py                 # Funções auxiliares, como excluir conta e buscar usuário
├── data
│   └── banco.py                 # Carrega e salva usuários em arquivo JSON
├── usuarios.json                # Arquivo onde os dados dos usuários ficam armazenados
```
---

## 🚀 Funcionalidades

- Cadastro de novos usuários
- Validação de campos (email, idade, username único, etc.)
- Senhas seguras com hash (usando `bcrypt`)
- Login com senha oculta
- Visualização e exclusão de perfil após login
- Dados persistidos em arquivo `.json`

---

## 🧰 Tecnologias

- Python 3.x
- bcrypt (para proteger as senhas com hash)
- getpass (para esconder a senha no terminal ao digitar)
- JSON (persistência)

---

🎯 Próximos passos
 
- [ ] Migrar a lógica para uma aplicação web com Flask
- [ ] Substituir o .json por um banco de dados
- [ ] Implementar validação de senha forte
- [ ] Adicionar validação de idade
- [ ] Feedback mais específico nos erros de cadastro
- [ ] Mensagem de logout ao sair do sistema
- [ ] Edição de perfil do usuário
- [ ] Recuperação de senha
- [ ] Diferentes tipos de usuário (admin, user)
- [ ] Testes unitários

