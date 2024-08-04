# Copyright (c) 2024, anwarpatelnoori and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Shop(Document):
	def before_save(self):
		shop_cateegory = self.shop_category.lower()
		shop_cateegory_fieldname = shop_cateegory.replace(' ','_')
		shop_rent =frappe.db.get_single_value('Shop Management Settings',shop_cateegory_fieldname)
		self.shop_rent = shop_rent
	def before_submit(self):
		# if (self.tenant_signature):
			today_date = frappe.utils.getdate()
			if(self.contract_start_date<=today_date <= self.contract_end_date ):
				self.status = 'Ongoing'
			elif (today_date>self.contract_end_date):
				frappe.throw('Contract End date should be greate than Today date')
				self.status = 'Expired'
			frappe.set_value('Shop',self.shop,'status','Occupied')
		
			
