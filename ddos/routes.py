from flask import Flask
from ddos import app

@app.route('/')
def home():
    return '<h1>Hello World</h1>'