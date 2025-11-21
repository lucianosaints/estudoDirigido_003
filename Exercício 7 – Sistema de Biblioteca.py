class Livro:
    """Representa um livro com título, autor e status de disponibilidade."""
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True  # Todo livro começa como disponível

    def __str__(self):
        """Retorna uma representação em string do livro."""
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' por {self.autor} (Status: {status})"

class Biblioteca:
    """Gerencia uma coleção de livros e suas operações."""
    def __init__(self, nome):
        self.nome = nome
        self.livros = []
        print(f"Biblioteca '{self.nome}' foi criada.")

    def adicionar_livro(self, titulo, autor):
        """Cria e adiciona um novo livro à coleção da biblioteca."""
        novo_livro = Livro(titulo, autor)
        self.livros.append(novo_livro)
        print(f"Livro {novo_livro} foi adicionado ao acervo.")

    def emprestar_livro(self, titulo):
        """Empresta um livro, se ele estiver disponível."""
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                if livro.disponivel:
                    livro.disponivel = False
                    print(f"\nO livro '{titulo}' foi emprestado com sucesso.")
                    return
                else:
                    # Regra de negócio: não emprestar livro já emprestado.
                    print(f"\nDesculpe, o livro '{titulo}' já está emprestado.")
                    return
        print(f"\nDesculpe, o livro '{titulo}' não foi encontrado em nosso acervo.")

    def devolver_livro(self, titulo):
        """Devolve um livro, marcando-o como disponível."""
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                if not livro.disponivel:
                    livro.disponivel = True
                    print(f"\nO livro '{titulo}' foi devolvido com sucesso.")
                    return
                else:
                    print(f"\nO livro '{titulo}' já estava disponível. Nenhuma ação necessária.")
                    return
        print(f"\nDesculpe, o livro '{titulo}' não pertence ao nosso acervo.")

    def listar_disponiveis(self):
        """Lista todos os livros que estão atualmente disponíveis para empréstimo."""
        print("\n--- Livros Disponíveis ---")
        disponiveis = [livro for livro in self.livros if livro.disponivel]
        if not disponiveis:
            print("Nenhum livro disponível no momento.")
        else:
            for livro in disponiveis:
                print(f"- {livro.titulo} (Autor: {livro.autor})")
        print("--------------------------")

# --- Exemplo de Uso ---

# 1. Criar uma biblioteca.
minha_biblioteca = Biblioteca("Biblioteca Central")

# 2. Adicionar livros ao acervo.
minha_biblioteca.adicionar_livro("O Senhor dos Anéis", "J.R.R. Tolkien")
minha_biblioteca.adicionar_livro("1984", "George Orwell")
minha_biblioteca.adicionar_livro("Dom Quixote", "Miguel de Cervantes")

# 3. Listar os livros disponíveis.
minha_biblioteca.listar_disponiveis()

# 4. Emprestar um livro.
minha_biblioteca.emprestar_livro("1984")

# 5. Tentar emprestar o mesmo livro novamente (teste da regra de negócio).
minha_biblioteca.emprestar_livro("1984")

# 6. Listar os livros disponíveis novamente para ver a mudança.
minha_biblioteca.listar_disponiveis()

# 7. Devolver o livro.
minha_biblioteca.devolver_livro("1984")

# 8. Listar os disponíveis uma última vez.
minha_biblioteca.listar_disponiveis()