from flask import render_template
from ddos import app
from ddos.forms import * 

@app.route('/')
def home():
    form=SubmitForm()
    return render_template('home.html',form=form)