import mysql.connector
import numpy as np

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Mihirmayuresh123!',
    database='scrapped_db'
)

mycursor = db.cursor(buffered=True)
mycursor1 = db.cursor(buffered=True)


def getamazon(shape):
    Q = 'SELECT name FROM product WHERE isprime != "NA"'
    mycursor.execute(Q)
    counter1 = 0
    for x in mycursor:
        if shape == counter1:
            break
        else:
            counter1 += 1
            yield x[0]


def getflipkart(shape):
    Q1 = 'SELECT name FROM product WHERE isprime = "NA"'
    mycursor1.execute(Q1)
    counter = 0
    for y in mycursor1:
        if counter == shape:
            break
        else:
            counter += 1
            yield y[0]


def retrivedata(ndarray_pairs):
    Q = 'SELECT * FROM product WHERE isprime != "NA"'
    mycursor.execute(Q)
    counter0 = 0
    Q1 = 'SELECT * FROM product WHERE isprime = "NA"'
    _ = 0
    for x in mycursor:
        mycursor1.execute(Q1)
        counter1 = 0
        for y in mycursor1:
            if [counter0, counter1] in ndarray_pairs.tolist():
                _ += 1
                print(_, '. ', x[1:3], '\n     ', y[1:3])
                print('-------------------------------------------------')
            counter1 += 1
        counter0 += 1
