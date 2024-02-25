from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__, template_folder="template")

@app.route('/success')
def success():
    return "Login Successful"

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["ps"]
        if name == "admin" and password == "123":
            return redirect(url_for("success"))
    # For unsuccessful POST or GET requests, render the admin.html template
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(debug=True)
