# Copyright (c) 2024, anwarpatelnoori and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns = [
        {
            'fieldname': 'airplane',
            'label': 'Airlines',
            'fieldtype': 'Link',
            'options': 'Airline'
        },
        {
            'fieldname': 'total_amount',
            'label': 'Total Amount',
            'fieldtype': 'Currency'
        }
    ]

    data = frappe.get_all('Airplane Ticket', fields=["total_amount", "airplane"], group_by='airplane')

    chart = {
        "data": {
            "labels": [x.airplane for x in data],
            "datasets": [{'values': [x.total_amount for x in data]}],
        },
        "type": 'donut'
    }

    total_profit = sum([x.total_amount for x in data])

    summary = [{
        "value": total_profit,
        "indicator": "Green" if total_profit > 0 else "Red",
        "label": "Total Revenue",
        "datatype": "Currency",
        "currency": "INR"
    }]

    return columns, data, None, chart, summary
