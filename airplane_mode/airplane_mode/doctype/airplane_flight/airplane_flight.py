# Copyright (c) 2024, anwarpatelnoori and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator
class AirplaneFlight(WebsiteGenerator):
	def before_submit(self):
		# print 20 new lines
		print("\n"*20)
		print("Before Submit")
		self.status = "Completed"
	def before_save(self):

		# Need Crew Members
		if len(self.flight_crew_members)<=0:
			frappe.throw('Please Add Flight Crew Members')
		# Not more than 5 Crew Members
		if len(self.flight_crew_members)>=5:
			frappe.throw('Flight Crew Members cannot be more than 5')

		# Atleast 1 Pilot and 1 Flight Attendants
		for i in self.flight_crew_members:
			if i.role == 'Pilot':
				break
			else:
				frappe.throw('Please Add a Pilot')
		for j in self.flight_crew_members:
			if j.role == 'Flight Attendants':
				break
			else:
				frappe.throw('Please Add Flight Attendants')
		# Maximum 2 Pilots and 3 Flight Att
		for k in self.flight_crew_members:
			pilot_counter = 0
			if k.role == 'Pilot':
				pilot_counter+=1
				if pilot_counter>=3:
					frappe.throw('Please Add Below 3 Pilot')
		for l in self.flight_crew_members:
			attendants_counter = 0
			if l.role == 'Flight Attendants':
				attendants_counter+=1
				if attendants_counter>=4:
					frappe.throw('Please Add Below 4 Flight Attendants')