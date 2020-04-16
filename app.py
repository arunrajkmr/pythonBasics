#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template

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

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

if __name__ == '__main__':
    app.run()
