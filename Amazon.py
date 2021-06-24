from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import urllib
import mysql.connector
import streamlit as st
i = 0
warn = 0
db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Mihirmayuresh123!',
    database='scrapped_db'
)

mycursor = db.cursor()
'''mycursor.execute('CREATE TABLE product(id int PRIMARY KEY AUTO_INCREMENT ,'
                 'name text, '
                 'price VARCHAR(10), isprime VARCHAR(2), '
                 'url text)')'''

# mycursor.execute('DROP TABLE product')

Q2 = 'SELECT * FROM product'
Q3 = 'TRUNCATE TABLE product'

mycursor.execute(Q3)
db.commit()


def ScrappingAmazon(KEYWORD, include_features=False):
    global warn
    while True:
        try:
            r = urllib.request.urlopen(f"https://www.amazon.in/s?k={KEYWORD}&ref=nb_sb_noss_2")
            product_page = r.read()
            soup = BeautifulSoup(product_page, 'lxml')
            body = soup.find('body', class_='a-aui_72554-c a-aui_accordion_a11y_role_354025-c '
                                            'a-aui_button_aria_label_markup_348458-t1 '
                                            'a-aui_csa_templates_buildin_ww_exp_337518-c '
                                            'a-aui_csa_templates_buildin_ww_launch_337517-c '
                                            'a-aui_csa_templates_declarative_ww_exp_337521-c '
                                            'a-aui_csa_templates_declarative_ww_launch_337520-c '
                                            'a-aui_dynamic_img_a11y_markup_345061-t1 '
                                            'a-aui_launch_cardui_a11y_fix_346896-c '
                                            'a-aui_markup_disabled_link_btn_351411-c a-aui_mm_desktop_exp_v2_353724-c '
                                            'a-aui_mm_desktop_gate_v2_353720-c a-aui_mm_desktop_targeted_exp_291928-c '
                                            'a-aui_mm_desktop_targeted_launch_291922-c a-aui_pci_risk_banner_210084-c '
                                            'a-aui_popover_trigger_add_role_350993-c a-aui_preload_261698-c '
                                            'a-aui_rel_noreferrer_noopener_309527-c a-aui_template_weblab_cache_333406-c '
                                            'a-aui_tnr_v2_180836-c')
            items_card = body.find('div', id='search')
            items = items_card.find_all('div',
                                        class_='sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col sg-col-4-of-20')
            i = 1
            Flag = True
            if len(items) == 0:
                items = items_card.find_all('div',
                                            class_='s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col '
                                                   'sg-col-12-of-16')
                Flag = False
            for item in items:  # picking all the items
                features = 'Feature flag was passed as "False", hence aborting!'
                try:
                    if Flag:
                        name = item.find('div', class_='a-section a-spacing-none a-spacing-top-small')
                    else:
                        name = item.find('h2', class_='a-size-mini a-spacing-none a-color-base s-line-clamp-2')
                    user_rating = item.find('div', class_='a-section a-spacing-none a-spacing-top-micro')
                    price = item.find('span', class_='a-offscreen')
                    try:
                        isprime = item.find('span', class_='aok-relative s-icon-text-medium s-prime')
                        isprime = isprime.find('i')['aria-label']
                        db_isprime = 'Y'
                    except KeyError:
                        isprime = False
                        db_isprime = 'N'
                    url = name.find('a')['href']
                    url = 'https://www.amazon.in' + url
                    usable_url = url.split('?')[0]  # taking only "GET" url
                    image_url = item.find('img', class_='s-image')['src']
                    if include_features:
                        while True:
                            '''For description'''
                            try:
                                r1 = urllib.request.urlopen(usable_url)
                                product_page1 = r1.read()
                                soup1 = BeautifulSoup(product_page1, 'lxml')

                                body1 = soup1.find('body')
                                dp = body1.find('div', id='ppd')
                                features = dp.find('div', id='featurebullets_feature_div')
                                features = features.text.replace('\n\n', '\n')
                                break
                            except urllib.error.HTTPError:
                                continue

                    '''print(f'{i}.Name: {name.text}\nPrice: {price.text}')
                    print(f'Amazon Prime Delivered Status: {isprime}')
                    print(f'Description: {features}')
                    print(f'URL: {url}')
                    print(
                        '-----------------------------------------------------------------------------------------------')'''
                    i += 1
                    mycursor.execute('INSERT INTO product(name, price, isprime, url, imageurl) VALUES (%s, %s, %s, %s, %s)',
                                     (name.text, price.text.split('₹')[1], db_isprime, usable_url, image_url))
                    db.commit()
                except:
                    continue
            #print(f'Fetched {i} entries from Amazon successfully!!!')
            st.sidebar.success(f'Fetched {i} entries from Amazon successfully!!!')
            break

        except urllib.error.HTTPError:
            #print('Trying to connect.....Please wait!!!')
            if warn < 1:
                st.sidebar.info('Establishing the connection.....Please wait!!!')
            warn += 1
            continue

        except AttributeError:
            st.error('Please enter valid search query, if problem persists, consider to enter detailed query')
            from distance_matrices import truncating
            truncating()
            break

        except TypeError:
            st.error('Please enter valid search query, if problem persists, consider to enter detailed query')
            from distance_matrices import truncating
            truncating()
            break