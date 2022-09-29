#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/")
def hello_world():
   return "Hello World"

@app.route("/menu/<coffee>")
def coffee_maker(coffee):
    return render_template("coffeemaker.html", coffee = coffee)

@app.route("/menu", methods = ["GET"])
def recipe():

   if request.args.get("nm"):
      coffee = request.args.get("nm")
      print("coffee found")
   else:
      coffee = "nofound"
   return redirect(url_for("nemu", coffee = coffee))

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE


