# Copyright (c) 2024, anwarpatelnoori and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator
class AirplaneFlight(WebsiteGenerator):
	def before_submit(self):
		# print 20 new lines
		print("\n"*20)
		print("Before Submit")
		self.status = "Completed"