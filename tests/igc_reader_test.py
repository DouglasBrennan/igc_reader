import logging

from flightlogs.igc_reader import read_igc
from django.test import TestCase


# Create your tests here.
class IgcReaderTest(TestCase):
	def test_read_igc(self):
		path_to_igc = 'tracks/2022-04-14-XFH-000-01.IGC'
		igc_data = read_igc.from_file(path_to_igc)
		self.assertIsInstance(igc_data, read_igc)

	def test_get_coordinates(self):
		path_to_igc = 'tracks/2022-04-14-XFH-000-01.IGC'
		igc_data = read_igc.from_file(path_to_igc)
		coordinates = igc_data.get_coordinates()
		self.assertIsInstance(coordinates, type([[int]]))
