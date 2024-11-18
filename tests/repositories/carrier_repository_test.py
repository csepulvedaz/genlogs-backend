import unittest
from api.repositories.carrier_repository import get_top_carriers_by_direction


class TestCarrierRepository(unittest.TestCase):

    def test_get_top_carriers_by_direction_nyc_to_dc(self):
        from_city = "New York"
        to_city = "Washington DC"
        carriers = get_top_carriers_by_direction(from_city, to_city)
        self.assertEqual(len(carriers), 3)
        self.assertEqual(carriers[0].name, "Knight-Swift Transport Services")
        self.assertEqual(carriers[0].trucks_per_day, 10)

    def test_get_top_carriers_by_direction_sf_to_la(self):
        from_city = "San Francisco"
        to_city = "Los Angeles"
        carriers = get_top_carriers_by_direction(from_city, to_city)
        self.assertEqual(len(carriers), 3)
        self.assertEqual(carriers[0].name, "XPO Logistics")
        self.assertEqual(carriers[0].trucks_per_day, 9)

    def test_get_top_carriers_by_direction_default(self):
        from_city = "Chicago"
        to_city = "Miami"
        carriers = get_top_carriers_by_direction(from_city, to_city)
        self.assertEqual(len(carriers), 2)
        self.assertEqual(carriers[0].name, "UPS Inc.")
        self.assertEqual(carriers[0].trucks_per_day, 11)

    def test_get_top_carriers_by_direction_partial_match(self):
        from_city = "New"
        to_city = "Washington"
        carriers = get_top_carriers_by_direction(from_city, to_city)
        self.assertEqual(len(carriers), 3)
        self.assertEqual(carriers[0].name, "Knight-Swift Transport Services")
        self.assertEqual(carriers[0].trucks_per_day, 10)

    def test_get_top_carriers_by_direction_case_insensitive(self):
        from_city = "new york"
        to_city = "washington dc"
        carriers = get_top_carriers_by_direction(from_city, to_city)
        self.assertEqual(len(carriers), 3)
        self.assertEqual(carriers[0].name, "Knight-Swift Transport Services")
        self.assertEqual(carriers[0].trucks_per_day, 10)


if __name__ == "__main__":
    unittest.main()
