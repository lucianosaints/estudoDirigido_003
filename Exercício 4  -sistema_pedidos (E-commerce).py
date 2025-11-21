class Produto:
    """Representa um item individual com nome e preço."""
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Pedido:
    """Representa um pedido que contém uma lista de produtos."""
    def __init__(self):
        # A lista de produtos vai guardar objetos da classe Produto.
        self.lista_de_produtos = []

    def adicionar_produto(self, produto):
        """Adiciona um objeto Produto à lista do pedido."""
        if isinstance(produto, Produto):  # Verifica se é uma instância da classe Produto
            self.lista_de_produtos.append(produto)
            print(f"Produto '{produto.nome}' adicionado ao pedido.")
        else:
            print("Erro: Apenas objetos da classe Produto podem ser adicionados.")

    def listar_produtos(self):
        """Lista todos os produtos no pedido."""
        if not self.lista_de_produtos:
            print("O pedido está vazio.")
            return
        
        print("--- Itens do Pedido ---")
        for produto in self.lista_de_produtos:
            print(f"Produto: {produto.nome}, Preço: R${produto.preco:.2f}")
        print("-----------------------")

    def calcular_valor_total(self):
        """Calcula e retorna o valor total de todos os produtos no pedido."""
        total = 0
        for produto in self.lista_de_produtos:
            total += produto.preco
        return total

# --- Exemplo de Uso ---

# 1. Crie instâncias da classe Produto.
produto1 = Produto("Camiseta", 49.90)
produto2 = Produto("Caneca", 15.50)
produto3 = Produto("Adesivo", 2.00)

# 2. Crie uma instância da classe Pedido.
meu_pedido = Pedido()

# 3. Adicione os produtos ao pedido.
meu_pedido.adicionar_produto(produto1)
meu_pedido.adicionar_produto(produto2)
meu_pedido.adicionar_produto(produto3)

# 4. Liste os produtos que estão no pedido.
meu_pedido.listar_produtos()

# 5. Calcule o valor total do pedido.
valor_total = meu_pedido.calcular_valor_total()
print(f"Valor Total do Pedido: R${valor_total:.2f}")