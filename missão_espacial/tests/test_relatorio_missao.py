import unittest
from relatorio_missao import RelatorioDeMissao
from robo_explorador import RoboExplorador

class TestRelatorioDeMissao(unittest.TestCase):
    def setUp(self):
        self.leituras = (("temperatura", -50), ("radiação", 2.5))
        self.relatorio = RelatorioDeMissao("Spirit", "Marte", 85, self.leituras)
        
    def test_heranca(self):
        self.assertIsInstance(self.relatorio, RoboExplorador)
        
    def test_resumo(self):
        self.assertEqual(self.relatorio.resumo(), ["temperatura: -50", "radiação: 2.5"])
        
    def test_contagem_leituras(self):
        self.assertEqual(self.relatorio.contagem_leituras(), 2)
        
    def test_relatorio_vazio(self):
        relatorio_vazio = RelatorioDeMissao("Empty", "Lua", 100, ())
        self.assertEqual(relatorio_vazio.resumo(), [])
        self.assertEqual(relatorio_vazio.contagem_leituras(), 0)

if __name__ == '__main__':
    unittest.main()