// Copyright (c) 2024, anwarpatelnoori and contributors
// For license information, please see license.txt

frappe.ui.form.on("Shop", {
    shop_category: function(frm) {
        let shop_category = frm.doc.shop_category.toLowerCase();
        let shop_field_name = shop_category.replace(/ /g, '_');

        frappe.call({
            method: "frappe.client.get_single_value",
            args: {
                'doctype': 'Shop Management Settings',
                'field': shop_field_name
            },
            callback: function(r) {
                if (r.message) {
                    frm.set_value('shop_rent', r.message);
                } else {
                    frappe.msgprint(__('Could not fetch value for the field: ') + shop_field_name);
                }
            }
        });
    }
});
