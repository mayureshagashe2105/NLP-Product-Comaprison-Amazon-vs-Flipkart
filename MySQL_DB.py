import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Mihirmayuresh123!',
    database='scrapped_db'
)

mycursor = db.cursor(buffered=True)


def getamazon():
    Q2 = 'SELECT * FROM product WHERE isprime != "NA"'
    mycursor.execute(Q2)
    for x in mycursor:
        yield x

def getflipkart():
    Q2 = 'SELECT * FROM product WHERE isprime = "NA"'
    mycursor.execute(Q2)
    for y in mycursor:
        print(y)
        yield y

mycursor.execute('SELECT * FROM product')
for i in mycursor:
    print(i)

