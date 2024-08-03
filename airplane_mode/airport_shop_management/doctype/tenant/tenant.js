// Copyright (c) 2024, anwarpatelnoori and contributors
// For license information, please see license.txt

frappe.ui.form.on("Tenant", {
	first_name:function(frm) {
        full_name(frm)
	},
    last_name:function(frm){
        full_name(frm)
    }
});
function full_name(frm){
    let full_name = ''
    if(frm.doc.last_name){
        full_name = `${frm.doc.first_name} ${frm.doc.last_name}`
    }
    else{
        full_name = frm.doc.first_name
    }
    frm.set_value('full_name',full_name)
}
