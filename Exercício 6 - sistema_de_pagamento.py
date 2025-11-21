class Usuario:
    """Representa um usuário com nome e saldo."""
    def __init__(self, nome, saldo=0):
        self.nome = nome
        self.saldo = saldo

    def adicionar_saldo(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"{self.nome} recebeu R${valor:.2f}. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Valor inválido para adicionar ao saldo.")

    def mostrar_saldo(self):
        print(f"Saldo de {self.nome}: R${self.saldo:.2f}")


class Pagamento:
    """Representa um pagamento feito a um usuário."""
    def __init__(self, usuario, valor):
        if not isinstance(usuario, Usuario):
            raise TypeError("Pagamento deve estar associado a um objeto Usuario.")
        self.usuario = usuario
        self.valor = valor
        self.status = "Pendente"

    def processar(self):
        if self.valor > 0:
            self.usuario.adicionar_saldo(self.valor)
            self.status = "Aprovado"
        else:
            self.status = "Recusado"
        print(f"Pagamento de R${self.valor:.2f} para {self.usuario.nome}: {self.status}")


# --- Exemplo de Uso ---
if __name__ == "__main__":
    ana = Usuario("Ana", 100)
    ana.mostrar_saldo()

    pagamento = Pagamento(ana, 250)
    pagamento.processar()

    ana.mostrar_saldo()
