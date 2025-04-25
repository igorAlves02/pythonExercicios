import unittest
from robo_explorador import RoboExplorador

class TestRoboExplorador(unittest.TestCase):
    def test_robo_explorador(self):
        robo = RoboExplorador("Spirit", "Marte", 85)
        self.assertEqual(str(robo), "Robô Spirit - Destino: Marte - Energia: 85%")
    
    def test_atributos(self):
        robo = RoboExplorador("Perseverance", "Marte", 95)
        # Como os atributos são privados, testamos através da representação em string
        self.assertIn("Perseverance", str(robo))
        self.assertIn("Marte", str(robo))
        self.assertIn("95%", str(robo))

if __name__ == '__main__':
    unittest.main()