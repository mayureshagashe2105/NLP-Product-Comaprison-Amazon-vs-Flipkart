from bs4 import BeautifulSoup
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


def ScrappingFlipkart(KEYWORD):
    while True:
        try:
            r = urllib.request.urlopen(f"https://www.flipkart.com/search?q={KEYWORD}")
            product_page = r.read()
            soup = BeautifulSoup(product_page, 'lxml')
            body = soup.find('body')
            roi = body.find('div', class_='_1YokD2 _3Mn1Gg', style='flex-grow:1;overflow:auto')
            divs = roi.find_all('div', class_='_1AtVbE col-12-12')
            i = 0
            price, url, Name1 = '', '', ''
            for div in divs[:10]:
                subdiv = div.find('div', class_='_4rR01T')
                if subdiv is None:
                    aas = div.find_all('a')
                    for a in aas:
                        Name = a.text
                        if Name == '' or Name == '1':
                            url = f'https://www.flipkart.com{a["href"]}'.split('?')[0]
                            display = f'https://www.flipkart.com{a["href"]}'

                        else:
                            if '₹' in Name:
                                price = Name.split('₹')[1]
                                '''print(f'Price: ₹{price}')
                                print(f'URL: {display}')
                                print("------------------------------")'''
                                i += 1
                                # print(f'{i}. ', end='')
                                temp = (Name1, price, 'NA', url)
                                mycursor.execute('INSERT INTO product(name, price, isprime, url) VALUES (%s, %s, %s, %s)', temp)
                                db.commit()
                            else:
                                Name1 = Name

                                #print(f'{Name}')


                else:
                    Name = subdiv.text
                    Des = div.find('div', class_='fMghEO')
                    Price = div.find('div', class_='_30jeq3 _1_WHN1')
                    url = f'https://www.flipkart.com{div.find("a")["href"]}'
                    # print(f'{i}. {Name}\nDescription: ')
                    for j in Des.text.split(","):
                        # print(j)
                        # print('\n')
                        pass
                    '''print(f'Price: {Price.text}')
                    print(f'URL : {url}')
                    print('------------------------------------------')'''
                    i += 1
                    mycursor.execute('INSERT INTO product(name, price, isprime, url) VALUES (%s, %s, %s, %s)', (Name, Price.text, "NA", url))
                    db.commit()
            print(f'Fetched {i} entries from Flipkart successfully!!!')
            break
        except urllib.error.HTTPError:
            print('Trying to connect.....Please wait!!!')
            continue
