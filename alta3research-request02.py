#!/usr/bin/env python3
import requests
from pprint import pprint


URL= "http://127.0.0.1:2224/menu/json"

response= requests.get(URL).json()

# user friendly format1 
pprint(response)
print()
print("-----------------------------------------------------------------------------")

# user friendly format2
for data in response:
    name = data['name']
    ingredients = data['ingredients']
    step = data['step']
    print()
    print(f" {name} \n ingridient: {ingredients} \n instruction: {step}")
    print()
    print("-----------------------------------------------------------------------------")
    
