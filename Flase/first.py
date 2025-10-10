from flask import Flask
'''
It creates an instance of the Flask class ,
which will be your WSGI (web server gateway Interface) applicaion 

'''


### WSGI application 

app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this Flask application by created in Madhav.. Thnak bro"

@app.route("/index")
def index():
    return "whelcome to the index page "


if __name__=="__main__":
    app.run(debug=True)