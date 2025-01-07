from flask import Flask

app = Flask(__name__)
  
@app.route("/")
def home():
    return "Hello I am Nishant, lets get started with FTP Deployment "
 
@app.route("/about")
def about():
    return "I am about"
 
if __name__ == "__main__":
    app.run(debug=True)
 