import requests
import unittest


class TestEndpoints(unittest.TestCase):
    def test_recipes_returns_expected_result(self):
        response = requests.get("http://localhost:5000/recipes")
        self.assertEqual(2, len(response.json()["data"]))
