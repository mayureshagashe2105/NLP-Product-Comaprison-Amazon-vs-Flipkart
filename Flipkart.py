from bs4 import BeautifulSoup
import time
import urllib.request
import urllib.error
import urllib

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
for div in divs:
    subdiv = div.find('div', class_='_4rR01T')
    if subdiv is None:
        aas = div.find_all('a')
        for a in aas:
            Name = a.text
            if Name == '' or Name == '1':
                if i != 0:
                    '''usable_url = f'https://www.flipkart.com{a["href"].split("?")[0]}'
                    r1 = urllib.request.urlopen(usable_url)
                    product_page1 = r1.read()
                    soup1 = BeautifulSoup(product_page1, 'lxml')
                    body1 = soup1.find('div', class_='_1YokD2 _3Mn1Gg')
                    print(body1.text)
                    exit(55)'''
                    print(f'https://www.flipkart.com{a["href"]}')
                print("------------------------------")
                i += 1
                print(f'{i}. ', end='')
            else:
                if '₹' in Name:
                    Name = Name.split('₹')[1]
                    print('Price: ₹', end='')
                print(f'{Name}')
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
