#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host='localhost',
    user='flask',
    password='flask',
    database='flaskdb'
)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']

        cur = mydb.cursor()
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)',
                (fullname, phone, email))

        mydb.commit()

        print("Conctact added")
        
        return redirect(url_for('index'))

@app.route('/edit')
def edit_contact():
    return 'Edit contact'

@app.route('/delete')
def delete_contact():
    cur = mydb.cursor()
    cur.execute('DELETE FROM contacts')

    mydb.commit()
    
    print('--All rows deleted--')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)
     

## Crear sesión (https://www.youtube.com/watch?v=IgCfZkR8wME&t=1471s - 33:47)
