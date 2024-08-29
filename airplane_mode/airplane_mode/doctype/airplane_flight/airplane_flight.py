# Copyright (c) 2024, anwarpatelnoori and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator
class AirplaneFlight(WebsiteGenerator):
	def before_validate(self):

		# Need Crew Members
		if len(self.flight_crew_members)<=0:
			frappe.throw('Please Add Flight Crew Members')

		# Atleast 1 Pilot and 1 Flight Attendants
		pilot_counter = 0
		attendants_counter = 0
		for i in self.flight_crew_members:
			if i.role == 'Pilot':
				pilot_counter+=1
			elif i.role =='Flight Attendants':
				attendants_counter +=1
		if pilot_counter<=0:
			frappe.throw('My Airplane is not Fully Automated 🙃 Add one Pilot')
		elif pilot_counter>=3:
			frappe.throw('No More Pilots 😇, Only 2 Allowed, remove extra')
		elif attendants_counter<=0:
			frappe.throw('Add 1 Flight Attendant,You Need Support in Sky 😉')
		elif attendants_counter>=4:
			frappe.throw('No More Flight Attendants 😇,Only 3 required, remove Extra')
