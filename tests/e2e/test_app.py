import requests
import unittest


class TestEndpoints(unittest.TestCase):
    def test_recipes_returns_expected_result(self):
        response = requests.get("http://localhost:5000/recipes")
        self.assertEqual(2, len(response.json()["data"]))

    def test_recipes_search_id_returns_expected_result_if_exist(self):
        response = requests.get("http://localhost:5000/recipes/2")
        self.assertEqual(2, response.json()["data"]["id"])

    def test_recipes_search_id_returns_expected_result_if_does_not_exis(self):
        response = requests.get("http://localhost:5000/recipes/0")
        self.assertEqual("recipe not found", response.json()["message"])
