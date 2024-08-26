import frappe

def all_cron_jobs():

    # daily cron job
    rent_reminder()
    check_contract_status()
    check_and_set_shop_status()

    # cronjob @ 27 day of every month
    current_datetime = frappe.utils.get_datetime()
    current_date = current_datetime.date()
    current_month_day = current_date.day
    if (current_month_day == 27):
        create_month_rent_doctype()


def rent_reminder():
    shop_manage_sett = frappe.get_doc('Shop Management Settings')
    if(shop_manage_sett.enable_rent_reminders==1):
        all_ongoing_contracts = frappe.get_list("Shop Contract", fields=["name", "contract_start_date","contract_end_date"], filters = {"status":"Ongoing"})
        current_datetime = frappe.utils.get_datetime()
        current_date = current_datetime.date()
        current_month_day = current_date.day
        for contract in all_ongoing_contracts:
            template = frappe.get_doc('Email Template','Rent Reminder')
            shop = contract['shop']
            tenant = contract['tenant']
            tenant_email_id = contract['tenant_email_id']
            shop_rent = contract['shop_rent']
            send_email = frappe.render_template(template.response,{'shop':shop,'tenant':tenant,'shop_rent':shop_rent})
            if (shop_manage_sett.reminder_frequency=="3 Day Before" ):
                if(current_month_day>=28):
                    frappe.send_email(recipients=tenant_email_id,subject=template.subject, message=send_email)
            elif(shop_manage_sett.reminder_frequency=="2 Day Before"):
                if(current_month_day>=29):
                    frappe.send_email(recipients=tenant_email_id,subject=template.subject, message=send_email)
            elif(shop_manage_sett.reminder_frequency=="1 Day Before"):
                if (current_month_day>=30):
                    frappe.send_email(recipients=tenant_email_id,subject=template.subject, message=send_email)
    else:
        pass

def check_contract_status():
    all_ongoing_contracts = frappe.get_list("Shop Contract", fields=["name", "contract_start_date","contract_end_date"], filters = {"status":"Ongoing"})
    current_datetime = frappe.utils.get_datetime()
    current_date = current_datetime.date()
    current_month_day = current_date.day
    for contract in all_ongoing_contracts:
        contract_name = contract['name']
        contract_end_date = contract['contract_end_date']  
        if(current_date>contract_end_date):
            contract_status = frappe.db.get_value('Shop Contract',contract_name,'status')
            if (contract_status == 'Ongoing'):
                frappe.db.set_value('Shop Contract',contract_name,'status','Expired')  

def check_and_set_shop_status():
    all_expired_contracts = frappe.get_list("Shop Contract", fields=["name", "contract_end_date", "shop"], filters={"status": "Expired"})
    shop_manage_sett = frappe.get_doc('Shop Management Settings')
    current_datetime = frappe.utils.get_datetime()
    current_date = current_datetime.date()
    current_month_day = current_date.day
    for contract in all_expired_contracts:
        contract_end_date = contract['contract_end_date']
        on_hold_date = None
        shop = contract['shop']
        shop_status = frappe.db.get_value('Shop',shop,'status')
        if (shop_status =='Occupied'):
            if shop_manage_sett.on_hold_days == '10 Days':
                if (current_month_day>=21):
                    frappe.db.set_value('Shop',shop,'status','On Hold')
                    on_hold_date =frappe.utils.add_to_date(contract_end_date,days=10)
            elif shop_manage_sett.on_hold_days == '6 Days':
                if (current_month_day>=25):
                    frappe.db.set_value('Shop',shop,'status','On Hold')
                    on_hold_date =frappe.utils.add_to_date(contract_end_date,days=6)
            elif shop_manage_sett.on_hold_days == '3 Days':
                if (current_month_day>=28):
                    frappe.db.set_value('Shop',shop,'status','On Hold')
                    on_hold_date =frappe.utils.add_to_date(contract_end_date,days=3)
        elif(shop_status == 'On Hold' and on_hold_date==current_date):
            frappe.db.set_value('Shop',shop,'status','Available')

            

def create_month_rent_doctype():
    all_ongoing_contracts = frappe.get_list("Shop Contract", fields=["name", "contract_start_date","contract_end_date"], filters = {"status":"Ongoing"})
    current_datetime = frappe.utils.get_datetime()
    current_date = current_datetime.date()
    current_month_day = current_date.day
    for contract in all_ongoing_contracts:
        contract_name = contract['name']
        contract_start_date = contract['contract_start_date']
        contract_end_date = contract['contract_end_date']
        if(contract_start_date<=current_date<=contract_end_date):
            shop_rent_doc = frappe.new_doc('Monthly Shop Rent')
            shop_rent_doc.shop_contract = contract_name
            shop_rent_doc.insert(ignore_permissions = True)
            shop_rent_doc.submit()
            frappe.db.commit()
        if(current_date>contract_end_date):
            contract_status = frappe.db.get_value('Shop Contract',contract_name,'status')
            if (contract_status == 'Ongoing'):
                frappe.db.set_value('Shop Contract',contract_name,'status','Expired')  
