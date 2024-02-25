from flask import Flask,render_template
app = Flask(__name__,template_folder="template")

@app.route("/<name>")
def home(name):
    return render_template("food.html",content = name)

@app.route("/")
def about():
    return render_template("content.html")
if __name__ == "__main__":
    app.run(debug=True)