from flask import Flask
app = Flask(__name__)

@app.route("/results")
def get():