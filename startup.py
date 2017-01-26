# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 14:15:44 2017

@author: kodi.rider
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
