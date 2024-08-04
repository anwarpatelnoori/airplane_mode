# Copyright (c) 2024, anwarpatelnoori and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RentPaymentEntry(Document):
	def before_submit(self):
		if (self.rent_paid <=self.rent_amount and not self.rent_paid <= 0):
			self.pending_rent = self.rent_paid -  self.rent_amount
		elif(self.rent_paid>self.rent_amount):
			frappe.throw(f'Paid Amount {self.rent_paid} is greater than Rent Amount {self.rent_amount}')
		elif(self.rent_paid <= 0):
			frappe.throw('You Must Pay Rent')

		frappe.db.set_value('Monthly Shop Rent',self.shop_rent,'rent_payment_entry',self.name)
		frappe.db.set_value('Monthly Shop Rent',self.shop_rent,'rent_paid',self.rent_paid)
		frappe.db.set_value('Monthly Shop Rent',self.shop_rent,'pending_rent',self.pending_rent)

		if (self.rent_paid<self.rent_amount and not self.rent_paid <= 0):
			frappe.db.set_value('Monthly Shop Rent',self.shop_rent,'status','Partially Paid')
		elif(self.rent_paid==self.rent_amount and not self.rent_paid <= 0):
			frappe.db.set_value('Monthly Shop Rent',self.shop_rent,'status','Paid')