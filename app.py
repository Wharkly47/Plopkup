# coding: utf-8

from flask import Flask, render_template, request, g
import sqlite3
import threading

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('phone_data.db')
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def create_table():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS phone_data (
                id INTEGER PRIMARY KEY,
                phone_number TEXT,
                name TEXT,
                address TEXT
            );
        ''')
        db.commit()
        print("Table 'phone_data' created successfully.")

def query_database(phone_number):
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        query = f"SELECT * FROM phone_data WHERE phone_number = '{phone_number}'"
        cursor.execute(query)
        result = cursor.fetchone()
        return result

@app.route('/')
def index():
    return render_template('phone_lookup.html')

@app.route('/lookup_phone', methods=['POST'])
def lookup_phone():
    phone_number = request.form.get('phoneNumber')
    result = query_database(phone_number)
    return render_template('phone_result.html', result=result)

if __name__ == '__main__':
    with app.app_context():
        create_table()  # Appel à la fonction pour créer la table
    app.run(debug=False)