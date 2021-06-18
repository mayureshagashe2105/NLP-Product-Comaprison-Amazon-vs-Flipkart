import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Mihirmayuresh123!',
    database='scrapped_db'
)

mycursor = db.cursor()

Q2 = 'SELECT * FROM product'

mycursor.execute(Q2)
for x in mycursor:
    print(x)

