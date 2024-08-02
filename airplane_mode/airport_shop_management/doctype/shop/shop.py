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

