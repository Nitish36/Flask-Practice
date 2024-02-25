#Message Flash

from flask import Flask,redirect,render_template,url_for,request,session,flash
from datetime import timedelta

app = Flask(__name__,template_folder="template")
app.secret_key = "1234"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/login",methods = ["POST","GET"])
def home():
    if request.method == "POST":
        name = request.form["nm"]
        session["name"] = name
        return redirect(url_for("user",name = name))
    else:
        return render_template("index.html")

@app.route("/<name>")
def user(name):
    if "name" in session:
        session.permanent = True
        name = session["name"]
        #flash(f"You are logged in as {name}","info")
        return f"<h1>{name}</h1>"
    else:
        flash("You are not logged in!!")
        return redirect(url_for("home"))

@app.route("/logout")
def logout():
    flash("Logged out successfully !!","info")
    session.pop("name", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)