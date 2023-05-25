from flask import Flask, render_template

app = Flask(__name__) #instance of flask class

@app.route("/") #root url
def main():
    return render_template("search.html")

if __name__ == "__main__":
    app.run(debug=True)