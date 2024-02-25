from flask import Flask,redirect,url_for,render_template,request,session,flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__,template_folder="template")
app.secret_key = "1234"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(100))

    def __init__(self,name):
        self.name = name

@app.route("/login",methods = ["POST","GET"])
def home():
    if request.method == "POST":
        name = request.form["nm"]
        session["name"] = name

        return redirect(url_for("user",name = name))
    else:
        return render_template("form.html")

@app.route("/<name>",methods = ["POST","GET"])
def user(name):
    if "name" in session:
        session.permanent = True
        name = session["name"]
        if request.method == "POST":
            name = request.form["nm"]
            session["name"] = name
        else:
            if "name" in session:
                name = session["name"]
        return f"<h1>{name}</h1>"
    else:
        flash("You are not logged in!!")
        return redirect(url_for("home"))

@app.route("/logout")
def logout():
    flash("Logged out successfully !!",category="info")
    session.pop("name",None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)