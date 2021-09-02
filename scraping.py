from selenium import webdriver
import csv
import requests
import os

driver = webdriver.Chrome('./driver/chromedriver.exe')
driver.get('http://books.toscrape.com/')

header = ['product_page_url','universal_ product_code (upc)','title','price_including_tax','price_excluding_tax','number_available','product_description','category','review_rating','image_url']
data = []

def extract_infos_from_one(index_of_product_on_page,ask_csv):
    product = driver.find_elements_by_class_name('image_container')
    product[index_of_product_on_page].click()
    product = driver.find_element_by_class_name('product_page')

    url = driver.current_url

    title = product.find_element_by_tag_name('h1').text

    table = driver.find_element_by_class_name('table-striped')
    elements = table.find_elements_by_tag_name('td')
    upc = elements[0].text

    price_in_tax = elements[3].text
    price_in_tax = price_in_tax.replace('£','')
    price_ex_tax = elements[2].text
    price_ex_tax = price_ex_tax.replace('£','')

    available = driver.find_element_by_class_name('availability').text
    nb_available = ''
    number = ['0','1','2','3','4','5','6','7','8','9']
    for i in available:
        if i in number:
            nb_available += i

    try:
        description = driver.find_element_by_xpath('//*[@id="content_inner"]/article/p').text
        remove_characters = ['“', '”','"','—','\'']

        for character in remove_characters:
            description = description.replace(character, "")

        description = description.replace('’',' ')
    except:
        description = 'Aucune Description'


    heading = driver.find_element_by_class_name('breadcrumb')
    category = heading.find_elements_by_tag_name('li')[2].text

    class_name = driver.find_element_by_class_name('star-rating').get_attribute('class')
    class_name = class_name.replace('star-rating ','')
    grade = ['Zero','One','Two','Three','Four','Five']
    for i in grade:
        if class_name == i:
            index = grade.index(i)
            class_name = number[index]

    img = driver.find_element_by_tag_name('img').get_attribute('src')

    response = requests.get(img)
    try:
        os.mkdir('./images/')
    except:
        pass
    try:
        os.mkdir(f'./images/{category}/')
    except:
        pass

    file = open(f"./images/{category}/{upc}.png", "wb")
    file.write(response.content)
    file.close()
    driver.back()

    if ask_csv:
        try:
            os.mkdir('./books/')
        except:
            pass
        with open(f'./books/{upc}.csv', 'w', encoding='UTF8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerow([url,upc,title,price_in_tax,price_ex_tax,nb_available,description,category,class_name,img])


    return([url,upc,title,price_in_tax,price_ex_tax,nb_available,description,category,class_name,img])

def extract_all_page(category):
    data = []
    category = category.lower()
    category = category.title()
    category = category.replace('And','and')
    category = category.replace('A Comment','a comment')
    list_of_li = driver.find_element_by_xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul')
    li = list_of_li.find_elements_by_tag_name('li')

    for l in li:
        if l.text == category:
            driver.find_element_by_link_text(category).click()
            break
        if l.text == 'Crime':
            raise ValueError("La catégorie demandée ne fait pas partie des catégories disponibles...")


    number_of_book = driver.find_element_by_xpath('//*[@id="default"]/div/div/div/div/form/strong').text
    number_of_book = int(number_of_book)
    try:
        os.mkdir('./categories/')
    except:
        pass
    with open(f'./categories/{category}.csv', 'w', encoding='UTF8',newline='') as f:
        for i in range(0,number_of_book):
            if i%20 == 0 and i != 0:
                driver.find_element_by_link_text('next').click()
            data.append(extract_infos_from_one(i%20,False))
        writer = csv.writer(f)
        writer.writerow(header)
        for databook in data:
            writer.writerow(databook)

def all_categories():
    list = []
    list_of_li = driver.find_element_by_xpath('//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul')
    li = list_of_li.find_elements_by_tag_name('li')
    for l in li:
        list.append(l.text)
    return list

def extract_all_site():
    list = all_categories()
    for cat in list:
        extract_all_page(cat)

extract_infos_from_one(0,True)
extract_all_page('travel')
extract_all_site()