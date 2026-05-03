# test_cities.py

import unittest
from city_functions import city_country


class TestCityCountry(unittest.TestCase):
    """Tests for the city_country function."""

    def test_city_country(self):
        """Does Santiago, Chile return Santiago, Chile?"""
        result = city_country("Santiago", "Chile")
        self.assertEqual(result, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()