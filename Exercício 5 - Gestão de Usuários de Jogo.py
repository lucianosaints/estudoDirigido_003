class Jogador:
    """Representa um jogador com nome, saldo e inventário de itens."""
    def __init__(self, nome, saldo_inicial=0):
        self.nome = nome
        self.saldo = saldo_inicial
        self.itens = []
        print(f"Jogador '{self.nome}' criado com saldo inicial de R${self.saldo:.2f}.")

    def adicionar_saldo(self, valor):
        """Adiciona um valor ao saldo do jogador."""
        if valor > 0:
            self.saldo += valor
            print(f"R${valor:.2f} adicionados. Novo saldo de '{self.nome}': R${self.saldo:.2f}.")
        else:
            print("O valor a ser adicionado deve ser positivo.")

    def comprar_item(self, item, preco):
        """Tenta comprar um item se o jogador tiver saldo suficiente."""
        if preco <= 0:
            print("O preço do item deve ser positivo.")
            return

        if self.saldo >= preco:
            self.saldo -= preco
            self.itens.append(item)
            print(f"'{self.nome}' comprou o item '{item}' por R${preco:.2f}.")
            print(f"Saldo restante: R${self.saldo:.2f}.")
        else:
            print(f"Saldo insuficiente para comprar '{item}'.")
            print(f"Saldo atual: R${self.saldo:.2f}, Preço do item: R${preco:.2f}.")

    def mostrar_inventario(self):
        """Exibe o saldo e os itens do jogador."""
        print(f"\n--- Inventário de {self.nome} ---")
        print(f"Saldo: R${self.saldo:.2f}")
        if not self.itens:
            print("Itens: (Nenhum item)")
        else:
            print(f"Itens: {', '.join(self.itens)}")
        print("--------------------------")


# --- Exemplo de Uso ---

# 1. Criar um novo jogador.
jogador1 = Jogador("Herói123", 50)

# 2. Adicionar mais saldo.
jogador1.adicionar_saldo(100)

# 3. Mostrar o inventário.
jogador1.mostrar_inventario()

# 4. Comprar alguns itens.
jogador1.comprar_item("Espada Mágica", 75)
jogador1.comprar_item("Poção de Cura", 20)

# 5. Tentar comprar um item caro demais.
jogador1.comprar_item("Armadura Lendária", 200)

# 6. Ver o inventário final.
jogador1.mostrar_inventario()