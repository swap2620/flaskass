from flask import Flask , render_template , request
import requests 

app = Flask(__name__)

@app.route("/")
def helloworld():
    return(f"Hello World")

@app.route("/home") 
def homepage():
    return render_template("homepage.html")

@app.route("/teams") 
def teampage():
    return render_template("teams.html")

@app.route("/schedule") 
def schedule():
    return render_template("schedule.html")

@app.route("/submit" , methods = ['POST' , 'GET'])
def name_email():
    url = request.form.get("ExternalLink")
    name = request.form.get("name")
    email = request.form.get("email")
    
    
    response = requests.get(url)       
    
    data = response.json()
    return f"data : {data} {name} {email}"
if __name__ == '__main__' : 
    app.run(host = '0.0.0.0' , port = 5002)