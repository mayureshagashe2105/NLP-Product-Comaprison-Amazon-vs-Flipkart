from bs4 import BeautifulSoup
import time
import urllib.request
import urllib.error
import urllib
import pandas as pd

def SearchStringCompatibility():
    KEYWORD = input('Enter a product name ')
    search_words = KEYWORD.split()
    search_string = ""
    for i in range(len(search_words)):
        search_string += search_words[i] + '+'
    KEYWORD = search_string[:-1]
    return KEYWORD


KEYWORD = SearchStringCompatibility()

while True:
    Name, Price, Is_Prime, URL = [], [], [], []
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
        print(f'Showing results for {KEYWORD}:\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        i = 1
        Flag = True
        if len(items) == 0:
            items = items_card.find_all('div',
                                        class_='s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col '
                                               'sg-col-12-of-16')
            Flag = False
        for item in items:
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
                except KeyError:
                    isprime = False
                url = name.find('a')['href']
                url = 'https://www.amazon.in' + url
                usable_url = url.split('?')[0]

                while True:
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

                print(f'{i}.Name: {name.text}\nPrice: {price.text}')
                print(f'Amazon Prime Delivered Status: {isprime}')
                print(f'Description: {features}')
                print(f'URL: {url}')
                print('--------------------------------------')
                i += 1
                Name.append(name.text[:10])
                Price.append(price.text)
                Is_Prime.append(isprime)
                URL.append(url)

            except:
                continue

        data = pd.DataFrame({'Name': Name, 'Price': Price, 'IS_Prime': Is_Prime, 'URL': URL})
        data = data.set_index('Name')
        print(data.head())
        print('Waiting for 3 mins to refresh the page././././')
        time.sleep(3 * 60)

    except KeyboardInterrupt:
        exit(0)

    except urllib.error.HTTPError:
        print('Trying to connect.....Please wait!!!')
        continue
