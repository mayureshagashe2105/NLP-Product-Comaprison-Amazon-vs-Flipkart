import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Mihirmayuresh123!',
    database='scrapped_db'
)

mycursor = db.cursor(buffered=True)


def getamazon(shape):
    Q2 = 'SELECT name FROM product WHERE isprime != "NA"'
    mycursor.execute(Q2)
    counter = 0
    for x in mycursor:
        if counter == shape:
            break
        yield x[0]
        counter += 1


def getflipkart(shape):
    Q2 = 'SELECT name FROM product WHERE isprime = "NA"'
    mycursor.execute(Q2)
    counter = 0
    for y in mycursor:
        if counter == shape:
            break
        yield y[0]
        counter += 1
