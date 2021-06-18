from bs4 import BeautifulSoup
import time
import urllib.request
import urllib.error
import urllib
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Mihirmayuresh123!',
    database='scrapped_db'
)

mycursor = db.cursor(buffered=True)

Q2 = 'SELECT * FROM product'


def SearchStringCompatibility():
    KEYWORD = input('Enter a product name ')
    search_words = KEYWORD.split()
    search_string = ""
    for i in range(len(search_words)):
        search_string += search_words[i] + '+'
    KEYWORD = search_string[:-1]
    return KEYWORD


KEYWORD = SearchStringCompatibility()

r = urllib.request.urlopen(f"https://www.flipkart.com/search?q={KEYWORD}")
product_page = r.read()
soup = BeautifulSoup(product_page, 'lxml')
body = soup.find('body')
roi = body.find('div', class_='_1YokD2 _3Mn1Gg', style='flex-grow:1;overflow:auto')
divs = roi.find_all('div', class_='_1AtVbE col-12-12')
i = 0
for div in divs[:10]:
    subdiv = div.find('div', class_='_4rR01T')
    if subdiv is None:
        aas = div.find_all('a')
        for a in aas:
            price = 0
            url = ''
            Name = a.text
            if Name == '' or Name == '1':
                if i != 0:
                    url = f'https://www.flipkart.com{a["href"]}'.split('?')[0]
                    print(f'https://www.flipkart.com{a["href"]}')
                print("------------------------------")
                i += 1
                print(f'{i}. ', end='')
            else:
                if '₹' in Name:
                    price = Name.split('₹')[1]
                    print(f'Price: ₹{price}')
                else:
                    print(f'{Name}')
            mycursor.execute('INSERT INTO product(name, price, isprime, url) VALUES (%s, %s, %s, %s)',
                             (Name, price, 'NA', url))
            db.commit()

    else:
        Name = subdiv.text
        Des = div.find('div', class_='fMghEO')
        Price = div.find('div', class_='_30jeq3 _1_WHN1')
        url = f'https://www.flipkart.com{div.find("a")["href"]}'
        print(f'{i}. {Name}\nDescription: ')
        for j in Des.text.split(","):
            print(j)
            print('\n')
        print(f'Price: {Price.text}')
        print(f'URL : {url}')
        print('------------------------------------------')
        i += 1
        mycursor.execute('INSERT INTO product(name, price, isprime, url) VALUES (%s, %s, %s, %s)',
                         (Name, Price.text, 'NA', url.split('?')[0]))
        db.commit()


mycursor.execute(Q2)
for x in mycursor:
    print(x)
