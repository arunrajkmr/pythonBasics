#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request
import math

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
    return 'Hello_World'

@app.route('/home')
def home():
    return render_template('home.html')
    
@app.route('/user')
def user():
    name ='raj'
    return render_template('user.html', title='User', message='Hello %s!' %name)
    
@app.route('/users/<name>')
def users(name):
    return render_template('user.html', title='User', message='Hello %s!' %name)
    
@app.route('/addition')
def add():
    return render_template('addition.html')

@app.route('/results',  methods=['POST'])
def results():
    if request.method == 'POST':
        firstNum = int(request.form['first_val'])
        secondNum = int(request.form['second_val'])
    return render_template('results.html', result=firstNum+secondNum)

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

if __name__ == '__main__':
    #app.debug = True;
    app.run('127.0.0.1', '4000', True)
