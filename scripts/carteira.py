from scripts.transacao import Transacao

class Carteira:
    def __init__(self):
        self.transacoes = []
    
    def adicionar(self, transacao):
        self.transacoes.append(transacao)
        return f"Transação adicionada: {transacao.resumo()}"
    
    def exibir_transacoes(self):
        if not self.transacoes:
            return "Nenhuma transação registrada."
        
        resultado = "\n===== HISTÓRICO DE TRANSAÇÕES =====\n"
        for i, transacao in enumerate(self.transacoes, 1):
            resultado += f"{i}. {transacao.resumo()}\n"
        resultado += "=================================="
        return resultado
    
    def saldo(self):
        return sum(t.valor for t in self.transacoes)
    
    def filtrar_por_categoria(self, categoria):
        transacoes_filtradas = [t for t in self.transacoes if t.categoria.lower() == categoria.lower()]
        
        if not transacoes_filtradas:
            return f"Nenhuma transação encontrada na categoria '{categoria}'."
        
        resultado = f"\n===== TRANSAÇÕES: {categoria.upper()} =====\n"
        for i, transacao in enumerate(transacoes_filtradas, 1):
            resultado += f"{i}. {transacao.resumo()}\n"
        
        total = sum(t.valor for t in transacoes_filtradas)
        resultado += "==================================\n"
        resultado += f"Total da categoria {categoria}: {total}"
        return resultado
    
    def gastos_totais(self):
        return abs(sum(t.valor for t in self.transacoes if t.valor < 0))
    
    def renda_total(self):
        return sum(t.valor for t in self.transacoes if t.valor > 0)
    
    def resumo_geral(self):
        total_transacoes = len(self.transacoes)
        renda = self.renda_total()
        gastos = self.gastos_totais()
        saldo_final = self.saldo()
        
        resultado = "\n====== RESUMO FINANCEIRO ======\n"
        resultado += f"Total de transações: {total_transacoes}\n"
        resultado += f"Renda total: R$ {renda:.2f}\n"
        resultado += f"Gastos totais: R$ {gastos:.2f}\n"
        resultado += f"Saldo final: R$ {saldo_final:.2f}\n"
        resultado += "==============================="
        return resultado
    
    def listar_categorias(self):

        if not self.transacoes:
            return "Não há transações cadastradas."
        
        categorias = set(t.categoria for t in self.transacoes)
        resultado = "\n===== CATEGORIAS =====\n"
        for i, categoria in enumerate(sorted(categorias), 1):
            resultado += f"{i}. {categoria}\n"
        resultado += "======================"
        return resultado