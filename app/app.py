from flask import Flask, render_template, redirect, url_for
import mysql.connector, random, datetime
import config as c

app = Flask(__name__)
app.secret_key = c.flask_secret_key

DATABASE_TABLE = 'question'
db = mysql.connector.connect(
    host = c.mysql_hostname,
    user = c.mysql_username,
    password = c.mysql_password,
    database = c.mysql_database
)
cursor = db.cursor()

@app.route('/')
def index():

    cursor.execute(f"SELECT * FROM {DATABASE_TABLE}")
    data = cursor.fetchall()
    print(data)
    
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)






