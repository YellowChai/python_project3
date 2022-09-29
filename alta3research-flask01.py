#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

import json

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)


coffeemenu = [
   {
      "name" : "Pumpkin Spice Latte",
      "ingredients": [
         "1/2 cup brewed coffee",
         "3/4 cup milk",
         "2-3 tablespoons pumpkin puree",
         "1-3 tablespoons maple syrup",
         "1/2 teaspoon vanilla extract",
         "1/2 teaspoon pumpkin pei spice"
      ],
      "step": [
         "1. Brew Coffee, and set the coffee aside and keep warm",
         "2. Warm the pumpkin Spiced Milk - over medium heat, war the mil, maple syrup, pumpkin pie spice, and pumpkin puree in a small saucepan. Whisk the ingredients until the mil begins to bubble on the sides. Turn off the heat and add the vanilla extract."
         "3. Blend the Milk Mixture in the saucepan."
         "4. Combine Mil and Coffee"
         "5. Enjoy! "
      ]
   }
]


# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/")
def hello_world():
   return "Hello World"

@app.route("/menu/<coffee>")
def coffee_maker(coffee):
    return render_template("coffeemaker.html", coffee = coffeemenu)

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


