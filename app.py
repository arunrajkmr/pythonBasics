#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, url_for, request
import math
import requests
import sqlite3
import random
from sqlite3 import Error
import os.path

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "pythondatabase.db")
database = "pythondatabase"

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
    
@app.route('/recrusive')
def recrusive():
    URL = "https://pc-json-collection-api.herokuapp.com/json/3"
    response = requests.get(URL)
    data = response.json()
    if len(data) > 0:
        conn = create_connection(db_path)
        print (conn)
        for key, values in data.items():
            if type(values) == dict:
                traversedic(conn, values, URL)
            else:
                print (str(values))
    cur = conn.cursor()
    cur.execute('SELECT * FROM task')
    rows = cur.fetchall()
    for row in rows:
        print(row)  
    return render_template ('results.html', result=data)

def traversedic(conn, dic, url):
    for key, value in dic.items():
        if(type(value) is dict):
            traversedic(conn, value, url)
        else:
            print (key + "-" + str(value))
            add_to_public_table(conn, key, value, url)

def add_to_public_table(conn, key, value, url):
    select_sql = ''' SELECT * FROM task WHERE key = :key AND value = :value'''
    task_select_obj = {
            'key' : key,
            'value': value
    }
    cur = conn.cursor()
    cur.execute(select_sql, task_select_obj)
    rows = cur.fetchall()
    if(len(rows) > 0):
        print('Already Data available')
    else:
        insert_sql = ''' INSERT INTO task (url, key, value) VALUES (:url, :key, :value) '''
        task_insert_obj = {
            'url' : url,
            'key' : key,
            'value': value
        }
        try:
            cur.execute(insert_sql, task_insert_obj)
            created_id = cur.lastrowid
        except sqlite3.IntegrityError as sqle:
            print("SQLite error : {0}".format(sqle))
        finally:
            conn.commit()
        print (created_id)

def main():
    sql_create_tasks_table = """ CREATE TABLE IF NOT EXISTS tasks (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        url text,
                                        key text NOT NULL,
                                        value text,
                                        UNIQUE (key, value)
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)  

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None
#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

if __name__ == '__main__':
    #app.debug = True;
    app.run('127.0.0.1', '4000', True)
