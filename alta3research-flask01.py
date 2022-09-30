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
         "Brew Coffee, and set the coffee aside and keep warm",
         "Warm the pumpkin Spiced Milk - over medium heat, war the mil, maple syrup, pumpkin pie spice, and pumpkin puree in a small saucepan. Whisk the ingredients until the mil begins to bubble on the sides. Turn off the heat and add the vanilla extract.",
         "Blend the Milk Mixture in the saucepan.",
         "Combine Mil and Coffee",
         "Enjoy! "
      ]
   },
   {
      "name": "Vanilla Latte",
      "ingredients":[
         "1/2 cup brewed coffee",
         "3/4 cup milk",
         "vanilla syrup", 
         "whipped cream"
      ],
      "step": [
         "Add the espresso to a mug",
         "Heat milk, stir in vanilla syrup, and froth",
         "Pour the vanilla milk over the espresso",
         "Top with foam, and whipped cream if desired"

      ]
   },
   {
      "name": "Charamel macchiato",
      "ingredients": [
         "14oz milk",
         "2 tbsp. vanilla syrup",
         "2oz espresso",
         "caramel sauce"
      ], 
      "step":[
         "Prepare the espresso",
         "warm up the milk and froth",
         "Pour the espresso into a cup",
         "Add vanilla and mil to the cup",
         "Pour the espresso on top of the frothy milk creating a mark on the foam",
         "Drizzle the caramel on top"
      ]
   }
]


# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/")
def hello_world():
   return "Hello World"

# search the coffee that user requested 
@app.route("/menu/<coffee>")
def coffee_maker(coffee):
   print("hit")
   for x in coffeemenu:
      if x['name'] == coffee:
         return render_template("coffeedetail.html", coffee = x)

@app.route("/menu/")
def coffee_list():
   return render_template("coffeelist.html", coffeemenu = coffeemenu)

# @app.route("/menu", methods = ["GET"])
# def recipe():
#    if request.args.get("nm"):
#       rescoffee = request.args.get("nm")
#       coffee = coffeemenu[rescoffee]
#       print(coffee)
#    else:
#       coffee = "nofound"
#    return redirect(url_for(coffee_maker,  coffee = coffee))

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application



