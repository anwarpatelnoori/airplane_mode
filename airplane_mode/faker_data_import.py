import frappe
from faker import Faker
import random
import string
import requests
from datetime import date
import calendar
fake = Faker('en_IN')

def import_all_data():
    print("""Making up funny fake people to test the app—it's like a having imaginary friends for practice!""")
    fake_airport()
    fake_shops()
    fake_tenant()
    fake_shop_contract()

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
    print('6 Fake Airport Created')

def fake_shops():
    shop_url = "https://api.unsplash.com/search/photos?client_id=-0IYW0fhhCOlRoB79UX_tZeAyjErmCf4ZANKamNxO7s&query=shop&per_page=30"
    image_json_data = requests.get(shop_url)
    shop_results = image_json_data.json().get('results',[])
    all_shop_image_urls =[]
    for i in shop_results:
        shop_image_url = i['urls']['small']
        all_shop_image_urls.append(shop_image_url)    
    current_airport = frappe.db.get_list('Airport',fields=['name'])
    airport_name  = []
    for a in current_airport:
        airport_name.append(a['name'])
    shop_category = ['Clothing Stores','Bookstores and Newsstands','Restaurants and Diners','Currency Exchange and Banks','Health and Pharmacy Stores', 'Gift Shops Rent']
    for j in all_shop_image_urls:
        ltr_4 = ''
        for k in range(4):
            ltr_4+= random.choice(string.ascii_uppercase)
            shop_number = f'{ltr_4}{random.randint(1,99)}'
            area = round(random.uniform(1,999),2)
        new_shop = frappe.new_doc('Shop')
        new_shop.status = 'Available'
        new_shop.shop_number = shop_number
        new_shop.shop_category = random.choice(shop_category)
        new_shop.airport = random.choice(airport_name)
        new_shop.area = area
        new_shop.shop_image = j
        new_shop.insert(ignore_permissions = True)
    frappe.db.commit()
    print('30 Fake Shops Created')

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
    print('30 fake Tenants  Created Using Unsplash api')

def fake_shop_contract():
    tenant = frappe.db.get_all('Tenant',fields = ['name'])
    availbale_shop = frappe.db.get_all('Shop',fields = ['name'],filters= {'status':'Available'})
    contracted_tenant = random.sample(tenant,20)
    availbale_shop  = random.sample(availbale_shop,20)
    start_year = 2024
    today_date = frappe.utils.getdate()
    for i in range(len(contracted_tenant)):
        # random cnotract duration
        start_month = random.randint(1, 12)
        contract_start_date = date(start_year, start_month, 1)
        end_month = random.randint(1, 24)
        contract_end_date = frappe.utils.add_months(contract_start_date, end_month)

        # create 20 Contract
        new_contract = frappe.new_doc('Shop Contract')
        new_contract.tenant = contracted_tenant[i]['name']
        new_contract.shop = availbale_shop[i]['name']
        new_contract.contract_start_date = contract_start_date
        new_contract.contract_end_date  = contract_end_date

        # set contract status
        if(contract_start_date<=today_date <=contract_end_date):
            new_contract.status = 'Ongoing'
        elif (today_date>contract_end_date):
            new_contract.status = 'Expired'

        # shop status occupied
        frappe.db.set_value('Shop',availbale_shop[i]['name'],'status','Occupied')
        
        new_contract.submit()
    frappe.db.commit()
    print('20 Fake Contracts Created')

def update_shop_image():
    shop_url = "https://api.unsplash.com/search/photos?client_id=-0IYW0fhhCOlRoB79UX_tZeAyjErmCf4ZANKamNxO7s&query=shop&per_page=30"    
    image_json_data = requests.get(shop_url)     
    shop_results = image_json_data.json().get('results',[])    
    all_shop_image_urls =[]    
    for i in shop_results:    
        shop_image_url = i['urls']['small']    
        all_shop_image_urls.append(shop_image_url)
    all_shop = frappe.get_all('Shop')   

    if len(all_shop) == len(all_shop_image_urls):
        for i, shop in enumerate(all_shop):
            shop_name = shop.name
            image_url = all_shop_image_urls[i]

            # Update the shop record with the image URL
            frappe.db.set_value('Shop', shop_name, 'shop_image', image_url)  # Replace 'image_url_field' with your actual field name

        frappe.db.commit()
        print("Images attached successfully!")
    else:
        print("The number of shops and images do not match.")















# SET SQL_SAFE_UPDATES = 0;
# delete from `tabTenant`;
# delete from `tabShop`;
# delete from `tabShop Contract`;
# delete from `tabMonthly Shop Rent`;
# delete from `tabRent Payment Entry`;
# SET SQL_SAFE_UPDATES = 1;