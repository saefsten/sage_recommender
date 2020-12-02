from flask import Flask, render_template, request
import ml_models

app = Flask(__name__)
# instantiating a Flask application
# "__name__" is a reference to the current script (application.py)


# @ notation is called a decorator function. it modifies the behavior of the function
# that occurs after it.
# any time somebody visits /index, trigger this function!!
@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")


# we can make our routes dynamic! This is the foundation of APIs. Also checkout: FastAPI
@app.route("/greet/<name>")
def greet(name):
    return render_template("greeting.html", name_html=name)


@app.route("/recommend")
def recommend():
    results = ml_models.simple_recommender(5)

    user_input = dict(request.args)
    movies = [user_input["movie1"], user_input["movie2"], user_input["movie3"]]
    ratings = [user_input["rating1"], user_input["rating2"], user_input["rating3"]]

    ### 1. Train your model (OR the model is already pre-trained)
    ### 2. Process the input, e.g. convert everything into numbers.... movie titles -> column numbers
    ### 3. Data Validation, e.g. spell check....
    ### 4. Convert the user input into an array of length of len(df.columns), ~9724
    ### 5. user_profile = nmf.transform(user_array). This user_profile is the "hidden feature profile" of the users for all hidden features
    ### 6. results = np.dot(user_profile, nmf.components_)
    ### 7. Sort the array, map the top N values to movie names
    ### 8. Return the titles. Also filter out movies the user has already seen.

    ##### BONUS: Insert new user data into the database.

    # results = ml_models.nmf_recommender(movies, ratings)

    return render_template("recommendations.html", results=results)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
