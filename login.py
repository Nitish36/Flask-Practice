from flask import Flask,redirect,url_for,request
app = Flask(__name__,template_folder="template")
@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form["nm"]
        email = request.form["em"]
        return redirect(url_for('success',name = user,email = email))
    else:
        user = request.args.get('nm')
        email = request.args.get('em')
        return redirect(url_for('success',name = user,email = email))

@app.route('/success/<name>/<email>')
def success(name,email):
    print("Email "+email)
    return "Hello "+name

if __name__ == '__main__':
    app.run(debug = True)