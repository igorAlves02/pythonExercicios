# main.py
from funcionarios import FuncionarioComum, Gerente
from sistema_rh import SistemaRH

def main():

    rh = SistemaRH()
    
    funcionarios_comuns = [
        FuncionarioComum("Alice", 300.0),
        FuncionarioComum("Igor", 250.00),
        FuncionarioComum("Gabriela", 500.00),
    ]
    
    gerentes = [
        Gerente("João", 10000.00, 250.00),
        Gerente("Karla", 12500.00, 500.00),
        Gerente("Lucas", 15000.00, 750.00)
    ]
    
    menor_tamanho = min(len(funcionarios_comuns), len(gerentes))
    
    for i in range(menor_tamanho):
        rh.set_funcionario(gerentes[i])
        rh.set_funcionario(funcionarios_comuns[i])
    
    for i in range(menor_tamanho, len(funcionarios_comuns)):
        rh.set_funcionario(funcionarios_comuns[i])
    
    for i in range(menor_tamanho, len(gerentes)):
        rh.set_funcionario(gerentes[i])
    
    print("\n=== Lista de Bônus de Funcionários ===")
    rh.listar_bonuses()
    print("=====================================")

if __name__ == "__main__":
    main()