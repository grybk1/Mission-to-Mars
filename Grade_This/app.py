from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/marsDB"
mongo = PyMongo(app)




# create route that renders index.html template
@app.route("/")
def echo():
    mars_data=mongo.db.mars_artifacts.find_one()
    return render_template ("index.html", marsData=mars_data)


@app.route("/scrape")
def scraper():
    mars_data=scrape_mars.scrape()
    mongo.db.mars_artifacts.insert_one(mars_data)
    return redirect("/", code=302)

@app.route("/Hemispheres")
def Hemispheres():
    mars_data=scrape_mars.getHemispheres()
    return render_template ("hemispheres.html", marsData1=mars_data[0],marsData2=mars_data[1],marsData3=mars_data[2],marsData4=mars_data[3])
   
if __name__ == "__main__":
    app.run(debug=True)
