# Copyright (c) 2024, anwarpatelnoori and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import *
import random


class ShopContract(Document):
	def before_save(self):
		contract_status(self)
		rent_payment_entry()
	def after_save(self):
		pass
	def before_submit(self):
		create_monthly_shop_rent(self)
def contract_status(self):
	today_date = frappe.utils.getdate()
	contract_start_date = frappe.utils.getdate(self.contract_start_date)
	contract_end_date = frappe.utils.getdate(self.contract_end_date) 
	if(contract_start_date<=today_date <=contract_end_date):
		self.status = 'Ongoing'
	elif (today_date>contract_end_date):
		self.status = 'Expired'
		# frappe.throw('Contract End date should be greate than Today date')
		pass
	frappe.set_value('Shop',self.shop,'status','Occupied')
def create_monthly_shop_rent(doc):
	current_contract = frappe.get_doc('Shop Contract',doc.name)
	diff = frappe.utils.month_diff(current_contract.contract_end_date,current_contract.contract_start_date)
	contract_start_date = current_contract.contract_start_date
	for i in range(diff):
		rent = frappe.new_doc('Monthly Shop Rent')
		rent.shop_contract = doc.name
		rent.rent_date = contract_start_date
		rent.submit()
		contract_start_date=frappe.utils.add_months(contract_start_date, 1)
	frappe.db.commit()
	frappe.msgprint(f'{diff} Monthly Shop Rent Doctypes are Created')


def rent_payment_entry():
    # all_shop_contract = frappe.get_all('Monthly Shop Rent', fields=['name'], filters={'status': ['in', ['Unpaid', 'Overdue', 'Partially Paid']]})
    monthly_rent = frappe.get_doc('Monthly Shop Rent', 'SR-0590-VQLS1-Bara-ARPT-08-24')
    shop_rent = monthly_rent.shop_rent
    current_pay = 0
    total_rent_paid = 0
    
    while total_rent_paid < shop_rent:
        payment_entry = frappe.new_doc('Rent Payment Entry')
        payment_entry.shop_rent = 'SR-0590-VQLS1-Bara-ARPT-08-24'
        payment_entry.pending_rent = shop_rent - total_rent_paid


        current_pay = random.randint(1, int(payment_entry.pending_rent))
        payment_entry.rent_paid = current_pay
        
        total_rent_paid += current_pay
        payment_entry.submit()
        frappe.db.commit()

    frappe.msgprint('Done')




   