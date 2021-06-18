import mysql.connector

db = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    passwd='Mihirmayuresh123!',
    database='scrapped_db'
)

mycursor = db.cursor()

# mycursor.execute('CREATE DATABASE scrapped_db')

