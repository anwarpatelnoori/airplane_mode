import frappe

def get_context(context):
    context.shops = frappe.get_all('Shop', filters={'status': 'Available'}, fields=['name', 'shop_rent', 'area','shop_category','shop_image','airport'])
    context.airports = frappe.get_all('Airport',fields=['name'])