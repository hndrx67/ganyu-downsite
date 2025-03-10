from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
import os
from werkzeug.utils import secure_filename
import uuid
from datetime import datetime


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('maintenance.html')
"""    
@app.route('/down')
def index():
    return render_template('webserverdown.html')
"""


if __name__ == '__main__':
    app.run(debug=True)
