import unittest
from igc_reader import igc_reader

def test_sum():
	assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
	assert sum((1, 2, 2)) == 6, "Should be 6"

if __name__ == "__main__":
	test_sum()
	test_sum_tuple()
	print("Everything passed")

# Create your tests here.
class IgcReaderTest(unittest.TestCase):
	def test_read_igc(self):
		path_to_igc = 'tracks/2022-04-14-XFH-000-01.IGC'
		igc_data = read_igc.from_file(path_to_igc)
		self.assertIsInstance(igc_data, read_igc)

	def test_get_coordinates(self):
		path_to_igc = 'tracks/2022-04-14-XFH-000-01.IGC'
		igc_data = read_igc.from_file(path_to_igc)
		coordinates = igc_data.get_coordinates()
		self.assertIsInstance(coordinates, type([[int]]))
