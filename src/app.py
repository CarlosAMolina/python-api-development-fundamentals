from flask import Flask, jsonify  # TODO , request

from http import HTTPStatus


app = Flask(__name__)

recipes = [
    {
        "id": 1,
        "name": "Egg Salad",
        "description": "An egg salad recipe",
    },
    {
        "id": 2,
        "name": "Tomato Pasta",
        "description": "A tomato pasta recipe",
    },
]


@app.route("/recipes", methods=["GET"])
def get_recipes():
    return jsonify({"data": recipes})


@app.route("/recipes/<int:recipe_id>", methods=["GET"])
def get_recipe(recipe_id: int):
    recipe = next((recipe for recipe in recipes if recipe["id"] == recipe_id), None)
    if recipe:
        return jsonify({"data": recipe})
    return jsonify({"message": "recipe not found"}), HTTPStatus.NOT_FOUND


if __name__ == "__main__":
    app.run()
