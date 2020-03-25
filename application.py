from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "What's up Hello World To New WEB APP using GIT & Devithub.com using DevOps tools!"
