
estoque = {}  

def adicionar_produto(estoque, nome, quantidade, preco):
    if quantidade > 0 and preco > 0:
        if nome in estoque:
            estoque[nome]["quantidade"] += quantidade
            estoque[nome]["preco"] = preco
        else:
            estoque[nome] = {"quantidade": quantidade, "preco": preco}
    else:
        print("Quantidade ou preço inválido!")


def remover_produto(estoque, nome, quantidade):
    if nome in estoque:
        if 0 < quantidade <= estoque[nome]["quantidade"]:
            estoque[nome]["quantidade"] -= quantidade
            if estoque[nome]["quantidade"] == 0:
                del estoque[nome]
        else:
            print("Quantidade para remover inválida!")
    else:
        print("Produto não encontrado no estoque!")


def valor_total(estoque):
    total = 0
    for produto in estoque.values():
        total += produto["quantidade"] * produto["preco"]
    return total


def listar_estoque(estoque):
    for nome, info in estoque.items():
        print(f"Produto: {nome}, Quantidade: {info['quantidade']}, Preço: R${info['preco']:.2f}")


# -------------------------------------------
# Exemplo de uso
# -------------------------------------------

adicionar_produto(estoque, "Caneta", 50, 2.5)
adicionar_produto(estoque, "Lápis", 30, 1.2)

listar_estoque(estoque)

print(f"Valor total do estoque: R${valor_total(estoque):.2f}")
