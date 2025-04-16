from transacao import Transacao
from carteira import Carteira

def main():
    # Criação das transações
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
    
    # Criação da carteira
    carteira = Carteira()
    
    # Adicionando as transações à carteira
    for transacao in transacoes:
        carteira.adicionar(transacao)
    
    # Exibir todas as transações
    print(carteira.exibir_transacoes())
    
    # Filtrar por categoria
    print("\nFiltrar por Alimentação:")
    print(carteira.filtrar_por_categoria("Alimentação"))
    
    # Listar todas as categorias
    print(carteira.listar_categorias())
    
    # Mostrar resumo geral
    print(carteira.resumo_geral())

if __name__ == "__main__":
    main()