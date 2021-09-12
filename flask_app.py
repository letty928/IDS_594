from flask import Flask

#Created a flask application with the name (__name__)
app = Flask(__name__)

#Creating a route for the website 
@app.route("/")
def home():
    return "Prediction"


#launches when you run the program 
if __name__ == '__main__':
    app.run()