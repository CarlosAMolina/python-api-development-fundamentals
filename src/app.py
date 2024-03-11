from flask import Flask, jsonify  # TODO , request

# TODO from http import HTTPStatus


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


if __name__ == "__main__":
    app.run()
