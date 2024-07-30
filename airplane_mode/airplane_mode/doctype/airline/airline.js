// Copyright (c) 2024, anwarpatelnoori and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airline", {
    refresh: function (frm) {
        if (frm.doc.website){
            let website = frm.doc.website;
            frm.add_web_link(website, 'Visit Website')
        }
    }
    
});
