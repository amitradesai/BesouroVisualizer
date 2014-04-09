import unittest
import besouro_visualizer
class TestBesouroVisualizer(unittest.TestCase):
	file_actions = "C:\Users\dfucci\Transporter\TDD\FSecure\Oulu\FSOU2801\Day5\MusicPhoneTask\.besouro\\20131101090638903\\actions.txt"
	def setUp(self):
		pass


	def test(self):
		self.assertEqual(besouro_visualizer.generate_first_episode(self.file_actions), 1383289599621//1000)

if __name__ == '__main__':
	unittest.main()