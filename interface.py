from flask import Flask, render_template, send_from_directory

app = Flask(__name__) #instance of flask class

@app.route("/") #root url
def main():
    return render_template("search.html")

#testings using output0.csv
@app.route("/output0.csv")
def retrieve_result():
    return send_from_directory("static", "output0.csv")
    #return send_from_directory("static", "result.csv")

if __name__ == "__main__":
    app.run(debug=True)