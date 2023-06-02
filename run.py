#Main file, combination of interface.py (frontend) and pylucene.py (backend)
#file modified based on the sample provided by Mr.SHIHAB RASHID from CS172 in UC riverside

#export FLASK_APP = main
#flask run -h 0.0.0.0 -p 8888

import logging, sys
logging.disable(sys.maxsize)

import os
import csv

from flask import Flask, render_template, send_from_directory

app = Flask(__name__) #instance of flask class

@app.route("/") #root url
def main():
    return render_template("search.html")

#output result stored in /static/result.csv on frontend
@app.route("/result.csv")
def retrieve_result():
    return send_from_directory("static", "result.csv")

if __name__ == "__main__":
    app.run(debug=True)