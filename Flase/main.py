from flask import Flask,render_template
'''
It creates an instance of the Flask class ,
which will be your WSGI (web server gateway Interface) applicaion 

'''


### WSGI application 

app=Flask(__name__)

@app.route('/')
def hey():
    return "<html><h1>Welcome</h1></html>"

@app.route("/index")
def index():
    # return "<html><H1>Welcome To ghe flask application </H1></html>"

    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
    
# @app.route("/index")
# def index():
#     return "whelcome to the index page "


if __name__=="__main__":
    app.run(debug=True)