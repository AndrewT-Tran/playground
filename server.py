from flask import Flask, render_template

app = Flask(__name__)





@app.route("/")
@app.route("/play")
def play():
    return render_template("index.html", num=4, color="blue")

@app.route("/<color>")
def justcolor(color):
    return render_template("index.html", num=5,color=color)
#just for fun, should reroute to just change the color
@app.route('/<num>')
@app.route("/play/<num>")
def num_squares(num):
    return render_template("index.html", num=int(num), color="blue")


@app.route("/play/<num>/<color>")
def color_squares(num, color):
    return render_template("index.html", num=int(num), color=color)


if (
    __name__ == "__main__"
):  # Ensure this file is being run directly and not from a different module
    app.run(debug=True)
    # Run the app in debug mode.
# app.run(debug=True, host="localhost", port=8000) changes the port if it above default is used.
