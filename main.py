from flask import Flask
app = Flask(__name__)   # create a flask app instance


@app.route("/")     #multiple routes to same route /home
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"


@app.route("/about")
def about():
    return "<h1>About Page</h1>"


if __name__ == '__main__':
    app.run(debug=True)