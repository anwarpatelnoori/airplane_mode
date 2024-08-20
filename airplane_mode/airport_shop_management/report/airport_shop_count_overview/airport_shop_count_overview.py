# Copyright (c) 2024, anwarpatelnoori and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	coulmns = [
		{
			'fieldname': 'airport',
			'label': 'Airport',
			'fieldtype': 'Link',	
			'options': 'Airport',
			'width': 150			
		},
		{
			'fieldname': 'no_of_shops',
			'label': 'Number of Shops',
			'fieldtype': 'Int',
			'width': 150
		},
		{
			'fieldname':'view_shop',
			'label': 'View Shops',
			'fieldtype': 'Data',
			'width': 150
		}
	]
	data = get_data(filters)
	return coulmns, data

def get_data(filters):
	conditions = "1=1"
	if filters.get('airport'):
		conditions += f" AND airport = '{filters.get('airport')}'"
	data = frappe.db.sql("""SELECT airport AS 'airport', COUNT(*) AS 'no_of_shops' FROM `tabShop` WHERE {conditions} GROUP BY airport;""".format(conditions=conditions),as_dict=1)
	return data
	
