# Copyright (c) 2024, anwarpatelnoori and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RentPaymentEntry(Document):
	def before_save(self):
		if(self.rent_paid>self.rent_amount):
			frappe.throw(f'Paid Amount {self.rent_paid} is greater than Rent Amount {self.rent_amount}')
		elif(self.rent_paid <= 0):
			frappe.throw('You Must Pay Rent')
	def before_submit(self):
		current_shop_rent = frappe.get_doc('Monthly Shop Rent',self.shop_rent)
		current_shop_rent.append('rent_payment_entry_logs',{'rent_payment_entry':self.name,'rent_amount':self.rent_amount,})
		current_shop_rent.save()
	def on_submit(self):
		print('\n\n\n\n\n\n')
		print('on_update_after_submit')
		total_rent_paid = 0
		total_shop_rent = frappe.get_doc('Monthly Shop Rent',self.shop_rent)
		for i in total_shop_rent.rent_payment_entry_logs:
			total_rent_paid+=i.rent_paid
			i.pending_rent = i.rent_amount-total_rent_paid
			# print('\n\n\n\n\n\n')
			# print(f'\nCurrent i.rent_amount: {i.rent_amount}')
			# print(f'Current i.rent_paid: {i.rent_paid}')
			# print(f'Cumulative total_rent_paid: {total_rent_paid}')
			# print(f'Calculated i.pending_rent: {i.pending_rent}\n')
			# print('\n\n\n\n\n\n')
		total_shop_rent.rent_paid = total_rent_paid
		total_shop_rent.pending_rent = total_shop_rent.shop_rent - total_rent_paid
		if total_shop_rent.rent_paid == self.rent_amount:
			total_shop_rent.status = 'Paid'
			# print('\n\n\n\n\n\n')
			# print(total_shop_rent.rent_payment_entry_logs[-1].pending_rent)
			# total_shop_rent.rent_payment_entry_logs[-1].pending_rent =0.000
		elif total_shop_rent.rent_paid <= self.rent_amount:
			total_shop_rent.status = 'Partially Paid'
		total_shop_rent.save()
		frappe.db.commit()