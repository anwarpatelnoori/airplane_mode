import frappe
from faker import Faker
import random
import string
import requests
fake = Faker('en_IN')
def fake_airport():
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
def fake_shops():
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

def fake_tenant():
    url = "https://api.unsplash.com/search/photos?client_id=-0IYW0fhhCOlRoB79UX_tZeAyjErmCf4ZANKamNxO7s&query=portrait&per_page=30"
    image_json_data = requests.get(url)
    results = image_json_data.json().get('results',[])
    indian_states = [
    "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan",
    "Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"
    ]
    all_image_urls =[]
    for i in results:
        image_url = i['urls']['small']
        all_image_urls.append(image_url)
    for i in all_image_urls:
        tenant_first_name = fake.first_name()
        tenant_last_name = fake.last_name()
        tenant_aadhar_number = random.randint(1,9999999999999)
        tenant_phone_number = fake.phone_number()
        tenant_country = 'India'
        tenant_state = random.choice(indian_states)
        tenant_address = fake.address()
        tenant_profile = i
        new_tenant = frappe.new_doc('Tenant')
        new_tenant.first_name = tenant_first_name
        new_tenant.last_name = tenant_last_name
        new_tenant.full_name = f'{tenant_first_name} {tenant_last_name}'
        new_tenant.aadhar_card_number = tenant_aadhar_number
        new_tenant.phone_number = tenant_phone_number
        new_tenant.attach_recent_photo = tenant_profile
        new_tenant.country = tenant_country
        new_tenant.state = tenant_state
        new_tenant.address =tenant_address
        new_tenant.insert(ignore_permissions=True)
    frappe.db.commit()
    print('30 Tenants  Created')
    


        


