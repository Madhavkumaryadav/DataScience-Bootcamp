### Buiding url dynamically 
## variable Rule 
# Jinja 2 tamplet Engine 

from flask import Flask,render_template,request


app=Flask(__name__)

@app.route('/')
def hey():
    return "<html><h1>Welcome</h1></html>"

@app.route("/index",methods=['GET'])
def index():
    # return "<html><H1>Welcome To ghe flask application </H1></html>"

    return render_template('index.html')
@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f"Hello! {name}"
    return render_template('form.html')


@app.route('/about')
def about():
    return render_template('about.html')
    
    
    
@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'<html><h1>Hello Welcome {name}</h1></html>'
    return render_template('form.html')

if __name__=="__main__":
    app.run(debug=True)