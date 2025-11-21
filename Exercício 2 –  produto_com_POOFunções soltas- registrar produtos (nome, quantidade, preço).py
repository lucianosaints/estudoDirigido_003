
class Produto:
    def __init__(self):
        # Cada produto será armazenado como: nome: {"quantidade": x, "preco": y}
        self.__estoque = {}

    def adicionar_produto(self, nome, quantidade, preco):
        if quantidade > 0 and preco > 0:  # verifica se a quantidade e o preço são válidos
            if nome in self.__estoque:
                self.__estoque[nome]["quantidade"] += quantidade # atualiza a quantidade
                self.__estoque[nome]["preco"] = preco  # Atualiza o preço se informado
            else:
                self.__estoque[nome] = {"quantidade": quantidade, "preco": preco} # adiciona novo produto
        else:
            print("Quantidade ou preço inválido!")

    def remover_produto(self, nome, quantidade): 
        if nome in self.__estoque:  #verifica se o produto existe
            if 0 < quantidade <= self.__estoque[nome]["quantidade"]:  #verifica se a quantidade é válida
                self.__estoque[nome]["quantidade"] -= quantidade #atualiza a quantidade
                if self.__estoque[nome]["quantidade"] == 0:  # remove o produto se a quantidade for zero
                    del self.__estoque[nome]  
            else:
                print("Quantidade para remover inválida!")
        else:
            print("Produto não encontrado no estoque!")

    def valor_total(self):
        total = 0
        for produto in self.__estoque.values():
            total += produto["quantidade"] * produto["preco"]
        return total

    def listar_estoque(self):
        for nome, info in self.__estoque.items(): # percorre o dicionário de estoque
            print(f"Produto: {nome}, Quantidade: {info['quantidade']}, Preço: R${info['preco']:.2f}")

# Exemplo de uso
p1 = Produto()
p1.adicionar_produto("Caneta", 50, 2.5)
p1.adicionar_produto("Lápis", 30, 1.2)
p1.listar_estoque()
print(f"Valor total do estoque: R${p1.valor_total():.2f}")
