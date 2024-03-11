from flask import Flask,render_template

app = Flask(__name__,template_folder="template")

@app.route("/")
def index2():
    return render_template('index2.html')

@app.route("/home2")
def home2():
    return render_template('home2.html')

@app.route("/about")
def about():
    sites = ["twitter","linkedin","Whatsapp","Instagram"]
    return render_template("about.html",sites = sites)

@app.route("/docs")
def docs():
    return render_template("docs.html")

if __name__ == '__main__':
    app.run(debug=True)