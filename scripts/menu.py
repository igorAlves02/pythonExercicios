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