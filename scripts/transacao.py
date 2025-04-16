class Transacao:
    def __init__(self, descricao, valor, categoria, data):
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria
        self.data = data
    
    def resumo(self):
        # Define o sinal para exibição
        sinal = "+" if self.valor >= 0 else ""
        return f"{self.descricao} | {sinal}{self.valor} | {self.categoria} | {self.data}"