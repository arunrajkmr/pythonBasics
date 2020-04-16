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
   return render_template('subtract.html', data=[{'operand':'+'}, {'operand':'-'}, {'operand':'*'}, {'operand':'/'}])

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
    
@app.route('/subtract')
def sub():
    return render_template('subtract.html', data=[{'operand':'+'}, {'operand':'-'}, {'operand':'*'}, {'operand':'/'}])

@app.route('/result',  methods=['POST'])
def result():
    firstNum = int(request.form['num1'])
    secondNum = int(request.form['num2'])
    result = firstNum + secondNum
    return render_template('results.html', result=result)

@app.route('/results',  methods=['POST'])
def results():
    if request.method == 'POST':
        print ( request.url )
        firstNum = int(request.form['num1'])
        secondNum = int(request.form['num2'])
        operand = request.form['operand_select']
        if operand == '+':
            result = firstNum + secondNum
        elif operand == '-':
            result = firstNum - secondNum
        elif operand == '*':
            result = firstNum * secondNum
        elif operand == '/':
            result = firstNum / secondNum
        else:
            result = 0
    return render_template('results.html', result=result)
    
@app.route('/calc')
def calc():
    return render_template('calc.html')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

if __name__ == '__main__':
    #app.debug = True;
    app.run('127.0.0.1', '4000', True)
