import mysql.connector
import numpy as np
import streamlit as st

db = mysql.connector.connect(
    host='localhost',
    user=USER_NAME,
    passwd=PASSWD,
    database=DB_USERNAME  # Your DB
)



mycursor = db.cursor(buffered=True)
mycursor1 = db.cursor(buffered=True)
mycursor2 = db.cursor(buffered=True)
mycursor3 = db.cursor(buffered=True)


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


def retrivedata(ndarray_pairs, con_dict, info, flag=False):
    # print(len(ndarray_pairs), "ok")
    global mycursor, mycursor1, mycursor2, mycursor3
    Q = 'SELECT * FROM product WHERE isprime != "NA"'
    Q1 = 'SELECT * FROM product WHERE isprime = "NA"'
    if not flag:
        mycursor.execute(Q)
        counter0 = 0
        # print('\n*****Matched Results:*****\n-------------------------------')
        if len(ndarray_pairs) is not 0:
            info.markdown('## **Matched Results**:')
        else:
            info.info(
                'Oops...seems like there weren\'t any great matches. Go to "All Products" page to see all the products seperately')
        __ = 0
        _ = 0
        for x in mycursor:
            mycursor1.execute(Q1)
            counter1 = 0
            for y in mycursor1:
                if [counter0, counter1] in ndarray_pairs.tolist():
                    _ += 1
                    info.markdown("<h3><centre>BEST MATCH</centre></h3>", unsafe_allow_html=True)
                    con = info.beta_columns(2)
                    con[0].markdown(f'''<!DOCTYPE html>
<html lang="en">
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div class="card" style="width: 18rem;">
  <img src="{x[-1]}" class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text"><b>Name:</b><font face="Comic sans MS">{x[1]}<br><b>Price:</b> {x[2]} Rs</font></p>
    <a href="{x[4]}" class="btn btn-primary">Go to Amazon</a>
  </div>
</div>
</body>
</html>''', unsafe_allow_html=True)
                    # print('*****BEST MATCH:*****')
                    # info.write(f'{x[:]} \n{y[:]}')
                    # info.table({'Name': [x[1], y[1]], 'Price': [x[2], y[2]], 'url': [x[4], y[4]]})
                    con[1].markdown(f'''<!DOCTYPE html>
<html lang="en">
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div class="card" style="width: 18rem;">
  <img src="{y[-1]}" class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text"><b>Name:</b><font face="Comic sans MS">{y[1]}<br><b>Price:</b> {y[2]} Rs</font></p>
    <a href="{y[4]}" class="btn btn-primary">Go to Flipkart</a>
  </div>
</div>
</body>
</html>''', unsafe_allow_html=True)
                    # print(_, '. ', x[1:3], '\n     ', y[1:3])
                    __ += 1
                    # print('##*RELATED MATCHES*')
                    info.markdown("<h3><centre>RELATED MATCHES</centre><h3/>", unsafe_allow_html=True)
                    retrivedata(np.array(con_dict[counter0]), {}, info, flag=True)
                    # print('---------------------------------------------')
                    info.markdown('<hr>', unsafe_allow_html=True)
                counter1 += 1
            counter0 += 1
    else:
        mycursor2.execute(Q)
        counter2 = 0
        name_li, price_li, url_li = [], [], []
        for x in mycursor2:
            mycursor3.execute(Q1)
            counter3 = 0
            for y in mycursor3:
                if [counter2, counter3] in ndarray_pairs.tolist():
                    # print(y[1:3])
                    info.markdown(f'''<!DOCTYPE html>
<html lang="en">
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div class="card mb-3" style="max-width: 540px;">
  <div class="row g-0">
    <div class="col-md-4">
      <img src="{y[-1]}" class="img-fluid rounded-start" alt="Image">
    </div>
    <div class="col-md-8">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text"><b>Name:</b> {y[1]}<br><b>Price:</b>{y[2]}</p>
        <p class="card-text"><small class="text-muted"><a href="{y[4]}" target="_blank">More Details</small></a></p>
      </div>
    </div>
  </div>
</div>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
</body>
</html>''',
                                  unsafe_allow_html=True)
                counter3 += 1
            counter2 += 1


def view_db(KEYWORD, omit=False):
    parts = st.beta_columns(2)
    parts[0].title(f'Amazon Products:')
    parts[1].title(f'Flipkart Products:')
    if KEYWORD == "":
        st.warning("Please enter search query first!!!")
    else:
        i = 0
        # print('*****Entries from Amazon related to search query:*****')
        mycursor1.execute('SELECT * FROM product WHERE isprime != "NA"')
        for item in mycursor1:
            i += 1
            # print(f'{i} . {item}\n--------------------')
            parts[0].markdown(f'''<!DOCTYPE html>
<html lang="en">
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div class="card" style="width: 18rem;">
  <img src="{item[-1]}" height="350px" class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text"><b>Name:</b><font face="Comic sans MS">{item[1][:60]}<br><b>Price:</b> {item[2]} Rs</font></p>
    <a href="{item[4]}" class="btn btn-primary">Go to Amazon</a>
  </div>
</div>
</body>
</html>''', unsafe_allow_html=True)

        i = 0
        # print('*****Entries from Flipkart related to search query:*****')
        mycursor1.execute('SELECT * FROM product WHERE isprime = "NA"')
        for item in mycursor1:
            i += 1
            # print(f'{i} . {item}\n--------------------')
            parts[1].markdown(f'''<!DOCTYPE html>
<html lang="en">
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div class="card" style="width: 18rem;">
  <img src="{item[-1]}" height="350px" class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text"><b>Name:</b><font face="Comic sans MS">{item[1][:60]}<br><b>Price:</b> {item[2]} Rs</font></p>
    <a href="{item[4]}" class="btn btn-primary">Go to Flipkart</a>
  </div>
</div>
</body>
</html>''', unsafe_allow_html=True)


def disconnect():
    global db
    db.close()


def count():
    mycursor1.execute('SELECT * FROM product WHERE isprime != "NA"')
    return len(mycursor1.fetchall())


def truncate():
    mycursor.execute('TRUNCATE TABLE product')
