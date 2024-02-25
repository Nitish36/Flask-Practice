from flask import Flask,request,redirect,url_for,render_template

app = Flask(__name__,template_folder='template')

@app.route('/answer/<num>/<squareofnum>')
def output(num, squareofnum):
    return f"The square of {num} is {squareofnum}"


@app.route('/',methods = ['GET','POST'])
def square():
    if request.method == 'POST':
        if request.form['num'] is None:
            return render_template('squarenum.html')
        elif request.form['num'] == '':
            return "Invalid Number"
        else:
            number = request.form['num']
            sq = int(number)*int(number)
            return render_template('answer.html',num = number,squareofnum = sq)
            #return redirect(url_for('output',num = number,squareofnum = sq))
    else:
        return render_template('squarenum.html')
if __name__ == "__main__":
    app.run(debug = True)