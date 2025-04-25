import pytest
from funcionarios import FuncionarioComum, Gerente
from sistema_rh import SistemaRH

def test_mostrar_bonus_funcionario_comum(capsys):
    sistema = SistemaRH()
    funcionario = FuncionarioComum("João", 2500.00)
    sistema.mostrar_bonus(funcionario)
    captured = capsys.readouterr()
    assert "O bonus do funcionário João é de 250.00" in captured.out

def test_mostrar_bonus_gerente(capsys):
    sistema = SistemaRH()
    gerente = Gerente("Maria", 4000.00, 200.00)
    sistema.mostrar_bonus(gerente)
    captured = capsys.readouterr()
    assert "O bonus do gerente Maria é de 1000.00" in captured.out

def test_listar_bonuses(capsys):
    sistema = SistemaRH()
    funcionario = FuncionarioComum("João", 2000.00)
    gerente = Gerente("Maria", 4000.00, 200.00)
    sistema.set_funcionario(funcionario)
    sistema.set_funcionario(gerente)
    sistema.listar_bonuses()
    captured = capsys.readouterr()
    assert "O bonus do funcionário João é de 200.00" in captured.out
    assert "O bonus do gerente Maria é de 1000.00" in captured.out