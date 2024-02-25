#HTTP Get Post method

from flask import Flask,redirect,render_template,url_for,request

app = Flask(__name__,template_folder="template")

@app.route("/login",methods = ["POST","GET"])
def home():
    if request.method == "POST":
        name = request.form["nm"]
        email = request.form["em"]
        age = request.form["ag"]

        return redirect(url_for("user",name = name, email = email,age = age))

    else:
        return render_template("index.html")

@app.route("/<name><email><age>")
def user(name,email,age):
    return f"Name: <h1>{name}</h1>\nEmail:<h1>{email}</h1>\nAge: <h1>{age}</h1>"

if __name__ == "__main__":
    app.run(debug=True)