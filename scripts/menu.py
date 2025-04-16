from transacao import Transacao
from carteira import Carteira

class Menu:
    def __init__(self):
        self.carteira = Carteira()
    
    def exibir_menu(self):
        print("\n===== GERENCIADOR FINANCEIRO =====")
        print("1. Adicionar nova transação")
        print("2. Exibir todas as transações")
        print("3. Filtrar transações por categoria")
        print("4. Ver resumo geral")
        print("5. Listar categorias disponíveis")
        print("0. Sair")
        print("=================================")
    
    def executar(self):
        self.carregar_dados_exemplo()
        
        while True:
            self.exibir_menu()
            escolha = input("Escolha uma opção: ")
            
            if escolha == "1":
                self.adicionar_transacao()
            elif escolha == "2":
                self.exibir_transacoes()
            elif escolha == "3":
                self.filtrar_por_categoria()
            elif escolha == "4":
                self.mostrar_resumo()
            elif escolha == "5":
                self.listar_categorias()
            elif escolha == "0":
                print("\nObrigado por usar o Gerenciador Financeiro. Até logo!")
                break
            else:
                print("Opção inválida! Por favor, tente novamente.")
    
    def adicionar_transacao(self):
        print("\n----- NOVA TRANSAÇÃO -----")
        descricao = input("Descrição: ")
        valor = float(input("Valor (use - para despesas): "))
        categoria = input("Categoria: ")
        data = input("Data (DD/MM/AAAA): ")
        
        transacao = Transacao(descricao, valor, categoria, data)
        resposta = self.carteira.adicionar(transacao)
        print(resposta)
    
    def exibir_transacoes(self):
        resultado = self.carteira.exibir_transacoes()
        print(resultado)
    
    def filtrar_por_categoria(self):
        categoria = input("\nDigite a categoria para filtrar: ")
        resultado = self.carteira.filtrar_por_categoria(categoria)
        print(resultado)
    
    def mostrar_resumo(self):
        resultado = self.carteira.resumo_geral()
        print(resultado)
    
    def listar_categorias(self):
        resultado = self.carteira.listar_categorias()
        print(resultado)
    
    def carregar_dados_exemplo(self):
        resposta = input("Deseja carregar transações de exemplo? (s/n): ").lower()
        if resposta == 's':
            transacoes = [
                Transacao("Compra de café", -10.50, "Alimentação", "15/10/2023"),
                Transacao("Salário", 2500.00, "Renda", "01/10/2023"),
                Transacao("Compra de livro", -50.00, "Educação", "20/10/2023"),
                Transacao("Aluguel", -1200.00, "Moradia", "05/10/2023"),
                Transacao("Supermercado", -300.00, "Alimentação", "10/10/2023"),
                Transacao("Venda de bicicleta", 500.00, "Renda Extra", "12/10/2023"),
                Transacao("Cinema", -30.00, "Lazer", "18/10/2023"),
                Transacao("Academia", -100.00, "Saúde", "08/10/2023"),
                Transacao("Freelance", 800.00, "Renda Extra", "22/10/2023"),
                Transacao("Doação", -50.00, "Caridade", "25/10/2023")
            ]
            
            for transacao in transacoes:
                self.carteira.adicionar(transacao)
            
            print("Transações de exemplo carregadas com sucesso!")