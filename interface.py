from flask import Flask

app = Flask(__name__) #instance of flask class

@app.route("/") #root url
def home():
    return "Hello, World!"
    
if __name__ == "__main__":
    app.run(debug=True)