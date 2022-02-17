#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
import mariadb
import os

app = Flask(__name__)

# MySQL Connection
mydb = mariadb.connect(
    host=os.environ.get('FLASK_DATABASE_HOST'),
    user=os.environ.get('FLASK_DATABASE_USER'),
    password=os.environ.get('FLASK_DATABASE_PASSWORD'),
    database=os.environ.get('FLASK_DATABASE'),
    port=3306
)

# Settings
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    cur = mydb.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    return render_template('index.html', contacts = data)

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

        flash('Contact added successfully')
        
        return redirect(url_for('index'))

@app.route('/edit/<id>')
def edit_contact(id):
    cur = mydb.cursor()
    cur.execute('SELECT * FROM contacts WHERE contact_ID = {0}'.format(id))

    data = cur.fetchall()

    print(data[0])
    return 'received'


@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mydb.cursor()
    cur.execute('DELETE FROM contacts WHERE contact_ID = {0}'.format(id))
    mydb.commit()

    flash('Contact removed successfully')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)
     

## Crear sesión (https://www.youtube.com/watch?v=IgCfZkR8wME&t=1471s - 51:34)
