import re

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def autenticar(self, email, senha):
        """Valida se o email e a senha conferem com os dados do usuário."""
        if email == self.email and senha == self.senha:
            print(f"Bem-vindo, {self.nome}!")
            return True
        
        print("Email ou senha incorretos.")
        return False


class SistemaLogin:
    def __init__(self, usuario):
        self.usuario = usuario

    def iniciar(self):
        print("=== Sistema de Login ===")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        self.usuario.autenticar(email, senha)


# --- Execução ---
usuario = Usuario("Luciano", "luciano@gmail.com", "1234")
sistema = SistemaLogin(usuario)
sistema.iniciar()
