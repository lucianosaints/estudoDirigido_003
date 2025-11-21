class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        print(f"Funcionário {self.nome} ({self.cargo}) contratado com salário de R${self.salario:.2f}.")

    def aumentar_salario(self, percentual):
        if percentual > 0:
            self.salario *= (1 + percentual / 100)
            print(f"Salário de {self.nome} aumentado em {percentual}%. Novo salário: R${self.salario:.2f}.")
        else:
            print("O percentual deve ser positivo.")

    def mostrar_detalhes(self):
        print(f"\nNome: {self.nome}\nCargo: {self.cargo}\nSalário: R${self.salario:.2f}")

# --- Exemplo de uso ---
func1 = Funcionario("Carlos Silva", "Desenvolvedor Sênior", 7500)
func1.mostrar_detalhes()
func1.aumentar_salario(10)
func1.mostrar_detalhes()
func1.aumentar_salario(-5)

#