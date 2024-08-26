# Copyright (c) 2024, anwarpatelnoori and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns =[
        {
            'fieldname':'name',
			'label': 'Monthly Shop Rent',
			'fieldtype':'Link',	
			'width': '320',
            'options':'Monthly Shop Rent' 
		},  
		{
            'fieldname': 'shop',
			'label': 'Shop',
			'fieldtype': 'Link',	
			'options': 'Shop',
			'width': 180	
		},
        {
            'fieldname':'airport',
			'label': 'Airport',
			'fieldtype':'Link',	
			'options': 'Airport',
			'width': '150'
		},
        {
            'fieldname':'tenant',
			'label': 'Tenant',
			'fieldtype':'Link',	
			'options': 'Tenant',
			'width': '210'
		},
        {
            'fieldname':'shop_rent',
			'label': 'Rent Amount',
			'fieldtype':'Currency',	
			'width': '150'
		},
        {
            'fieldname':'pending_rent',
			'label': 'Pending Rent',
			'fieldtype':'Currency',	
			'width': '150'
		}
	]
    data = get_data(filters)
    return columns,data


def get_data(filters):
    conditions = "1=1"
    if filters.get('airport'):
        conditions += f" AND shp.airport = '{filters.get('airport')}'"
    if filters.get('shop'):
        conditions += f" AND shop = '{filters.get('shop')}'"

    if filters.get('tenant'):
        conditions += f" AND tenant = '{filters.get('tenant')}'"
    data = frappe.db.sql("""
                    		select 
                    		    msr.shop,msr.tenant,msr.pending_rent,shp.airport,msr.name,msr.shop_rent
                    		from 
                    		    `tabMonthly Shop Rent` msr
							join
								`tabShop` shp
							on
                         		msr.shop = shp.name
                    		where 
                    		    msr.status = 'Partially Paid' and {conditions};
                    	""".
                        format(conditions=conditions),
                        as_dict=True)
    
    return data
