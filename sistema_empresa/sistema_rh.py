from funcionarios import Funcionario, FuncionarioComum, Gerente

def logar_acao(func):
    def wrapper(*args, **kwargs):
        funcionario = args[1]
        bonus = func(*args, **kwargs)
        
        cargo = "funcionário"
        if isinstance(funcionario, Gerente):
            cargo = "gerente"
        
        print(f"O bonus do {cargo} {funcionario.get_nome()} é de {bonus:.2f}")
        return bonus
    return wrapper


class SistemaRH:
    def __init__(self):
        self.__lista_de_funcionarios = []
    
    def set_funcionario(self, funcionario: Funcionario):
        self.__lista_de_funcionarios.append(funcionario)
    
    @logar_acao
    def mostrar_bonus(self, funcionario: Funcionario) -> float:
        return funcionario.calcular_bonus()
    
    def listar_bonuses(self):
        for funcionario in self.__lista_de_funcionarios:
            self.mostrar_bonus(funcionario)