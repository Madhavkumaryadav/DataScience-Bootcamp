from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hey():
    return "<html><h1>Welcome</h1></html>"

@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello! {name}"
    return render_template('form.html')


@app.route('/about')
def about():
    return render_template('about.html')


# ---------------------------
# ✅ Variable Rule Example
# ---------------------------
@app.route('/success/<score>')
def success(score):
    score = float(score)
    res = "PASSED" if score >= 50 else "FAILED"
    return render_template('result.html', results=score, status=res)



@app.route('/successer/<int:score>')
def successer(score):
    res = "PASSED" if score >= 50 else "FAILED"
    exp = {'score': score, 'res': res}
    return render_template('result1.html', results=exp)


# ---------------------------
# ✅ if condition example
# ---------------------------
@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result.html', results=score)


@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html', results=score)


# ---------------------------
# ✅ Form Submission & URL Building
# ---------------------------
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    total_score = 0
    if request.method == 'POST':
        # ✅ FIXED: use [] instead of ()
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])

        total_score = (science + maths + c + data_science) / 4

        # Dynamically redirect based on result
        
    else:
        return render_template('getresult.html')
    return redirect(url_for('success', score=total_score))


if __name__ == "__main__":
    app.run(debug=True)
