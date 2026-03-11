from flask import Flask
import time
import math

app = Flask(__name__)

@app.route("/")
def home():
    # Artificial CPU load
    
