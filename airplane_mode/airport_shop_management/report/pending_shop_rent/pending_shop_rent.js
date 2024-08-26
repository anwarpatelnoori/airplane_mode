// Copyright (c) 2024, anwarpatelnoori and contributors
// For license information, please see license.txt

frappe.query_reports["Pending Shop Rent"] = {
	"filters": [
		{
			'fieldname': 'airport',
			'label': 'Airport',
			'fieldtype': 'Link',
			'options': 'Airport',
			'width': '150',
		},
		{
			'fieldname': 'shop',
			'label': 'Shop',
			'fieldtype': 'Link',
			'options': 'Shop',
			'width': '150',
		},
		{
			'fieldname': 'tenant',
			'label': 'Tenant',
			'fieldtype': 'Link',
			'options': 'Tenant',
			'width': '150',
		},
	],
	onload(report) {		
		setTimeout(function() {
			$('.dt-row.dt-row-filter').remove(); 
		}, 50);
	}
};
