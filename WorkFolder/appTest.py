from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/marsDB"
mongo = PyMongo(app)

@app.route("/")
def home_page():
    # online_users = mongo.db.users.find({"online": True})
    doc = mongo.db.marsDB.insert_one({'abcd':'abcd'})
    return render_template("index.html", 
                           MarsNewsTag="MARS NEWS",
                           FeaturedImageTag="Sweet Image",
                           WeatherTag="Great Weather",
                           FactsTag="Nothing but the FACTS" )


if __name__ == '__main__':
    app.run(debug=True)
