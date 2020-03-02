from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars



mars_data=scrape_mars.getHemispheres()
for dict_item in mars_data:
  for key in dict_item:
    print (dict_item[key])

for x in mars_data:
     print(x)
     
print ('----------------')
print (mars_data[0])