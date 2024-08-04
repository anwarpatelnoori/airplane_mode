import frappe

all_ongoing_contracts = frappe.get_list("Shop Contract", fields=["name", "test_contract_start","test_contract_end"], filters = {"status":"Ongoing"})
current_time = frappe.utils.now_datetime()
for contract in all_ongoing_contracts:
    contract_name = contract['name']
    test_contract_start = contract['test_contract_start']
    test_contract_end = contract['test_contract_end']
    if(test_contract_start<=current_time<=test_contract_end):
        shop_rent_doc = frappe.new_doc('Monthly Shop Rent')
        shop_rent_doc.shop_contract = contract_name
        shop_rent_doc.insert(ignore_permissions = True)
        shop_rent_doc.submit()
        frappe.db.commit()
    if(current_time>test_contract_end):
        frappe.db.set_value('Shop Contract',contract_name,'status','Expired')