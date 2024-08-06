# Copyright (c) 2024, anwarpatelnoori and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ShopContract(Document):
	def before_save(self):
			# if (self.tenant_signature):
				today_date = frappe.utils.getdate()
				contract_start_date = frappe.utils.getdate(self.contract_start_date)
				contract_end_date = frappe.utils.getdate(self.contract_end_date) 
				if(contract_start_date<=today_date <=contract_end_date):
					self.status = 'Ongoing'
				elif (today_date>contract_end_date):
					frappe.throw('Contract End date should be greate than Today date')
					pass
				frappe.set_value('Shop',self.shop,'status','Occupied')