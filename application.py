from flask import Flask, render_template, request
import ml_models

app = Flask(__name__)


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/greet/<name>")
def greet(name):
    return render_template("greeting.html", name_html=name)


@app.route("/recommend")
def recommend():
    results = ml_models.simple_recommender(5)

    user_input = dict(request.args)
    movies = [user_input["movie1"], user_input["movie2"], user_input["movie3"]]
    ratings = [user_input["rating1"], user_input["rating2"], user_input["rating3"]]

    return render_template("recommendations.html", results=results)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
