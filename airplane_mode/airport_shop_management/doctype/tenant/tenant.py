# Copyright (c) 2024, anwarpatelnoori and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Tenant(Document):
	def before_validate(self):
		full_name_and_email(self)


def full_name_and_email(doc):
	if doc.last_name: 	
		doc.full_name = f"{doc.first_name} {doc.last_name}"
	else:
		doc.full_name = doc.first_name
	doc.email = f"anwar+{doc.first_name.lower().replace(' ','')}@standardtouch.com"