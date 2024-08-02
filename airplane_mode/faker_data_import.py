import frappe
from faker import Faker
import random
import string
fake = Faker('en_IN')
def airport():
    for i in range (6):
        city = fake.city()
        country = 'India'
        name = f'{city} Airport'
        c_abb = city[:4]
        code = f'{c_abb}-ARPT'
        airport = frappe.new_doc('Airport')
        airport.name = name
        airport.code = code
        airport.city = city
        airport.country = country
        airport.insert(ignore_permissions = True)
    frappe.db.commit()
    print('6 Airport Created')
def shops():
    current_airport = frappe.db.get_list('Airport',fields=['name'])
    airport_name  = []
    for a in current_airport:
        airport_name.append(a['name'])
    shop_category = ['Clothing Stores','Bookstores and Newsstands','Restaurants and Diners','Currency Exchange and Banks','Health and Pharmacy Stores', 'Gift Shops Rent']
    for i in range(40):
        ltr_4 = ''
        for i in range(4):
            ltr_4+= random.choice(string.ascii_uppercase)
            shop_number = f'{ltr_4}{random.randint(1,99)}'
            area = round(random.uniform(1,999),2)
        new_shop = frappe.new_doc('Shop')
        new_shop.status = 'Available'
        new_shop.shop_number = shop_number
        new_shop.shop_category = random.choice(shop_category)
        new_shop.airport = random.choice(airport_name)
        new_shop.area = area
        new_shop.insert(ignore_permissions = True)
    frappe.db.commit()
    print('40 Shops Created')
