from flask import Flask,flash,url_for,render_template,request,redirect

app = Flask(__name__,template_folder="template")
app.secret_key = "123"
@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/login2",methods = ["GET","POST"])
def login2():
    if request.method == "POST":
        passcode = request.form["pass"]
        if passcode == "123":
            flash("Logged in Successfully")
            return redirect(url_for("profile"))
        else:
            flash("Invalid Login")
            return redirect(url_for("profile"))
    return render_template("login2.html")

if __name__ == "__main__":
    app.run(debug=True)