// Copyright (c) 2024, anwarpatelnoori and contributors
// For license information, please see license.txt

frappe.query_reports["Airport Shop Count Overview"] = {
	"filters": [
		{
			'fieldname': 'airport',
			'label': 'Airport',
			'fieldtype': 'Link',
			'options': 'Airport',
			'width': '150',
		}
	],
	formatter:function(value, row, column, data, default_formatter) {
		let airport = data.airport
		if (column.fieldname ==='view_shop'){
			const view_shop_button = `<button class="btn btn-default btn-xs" onclick = "frappe.set_route('List','Shop',{'airport':'${airport}'})">View</button>`;
			value = view_shop_button
		}
		return default_formatter(value, row, column, data);
	}
};
