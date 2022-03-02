import datetime as dt
import numpy as np
import pandas as pd

# dependencies to access the sqlite DB
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, redirect, url_for, render_template, jsonify, request, session, flash

engine = create_engine("sqlite:///sqlite_db/mhp_db.sqlite")
Base = automap_base()
Base.prepare(engine, reflect = True)

City = Base.classes.city
Incomes = Base.classes.income
Mental = Base.classes.mental

session = Session(engine)

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"]) 
def user_input_info():
    if request.method == "POST":
        user_input = request.form["nm"]
        return render_template("Results.html")
    else:
        return render_template("index.html")


@app.route("/About")
def about():
    return render_template("About.html")

@app.route("/Team")
def team():
    return render_template("Team.html")

# @app.route("/<name>")
# def something(name):
#     return render_template("index.html", content=name, r=2)

if __name__ == "__main__":
    app.run(debug = True)






# @app.route('/')
# def welcome():
#     return(
#      '''
#     Welcome to the Mental Health Predictor! <br/>
#     Available Routes: <br/>
#     /mhp_predictor/v1.0/City_Population_Data <br/>
#     /mhp_predictor/v1.0/Income_Data <br/>
#     /mhp_predictor/v1.0/Mental_Health_Data <br/>
#     '''   )

# @app.route("/mhp_predictor/v1.0/City_Population_Data")
# def cities():
#     #make the query
#     city_df_query = session.query(City.city, City.state_id, City.state_name, City.population, City.density).all()
#     #make the df
#     city_df = pd.DataFrame(city_df_query, columns=['City','State_ID', 'State_Name', 'Population', 'Density'])
#         #city_df.set_index(city_df['City'], inplace= True)
#     #make the json structure?
#     bc_jsonify = {
#         city_df['City']:[
#             {"State ID": city_df['State_ID'],
#             "State Name": city_df['State_Name'],
#             "Population": city_df['Population'],
#             "Density": city_df['Density']}
#         ]
#         }
#     return jsonify(bc_jsonify)