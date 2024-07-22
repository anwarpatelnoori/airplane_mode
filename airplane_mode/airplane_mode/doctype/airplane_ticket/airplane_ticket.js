// Copyright (c) 2024, anwarpatelnoori and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) {
        add_custom_button(frm)
	},
});
function add_custom_button(frm){
    frm.add_custom_button(('Assign Seat'), function(){
        frappe.prompt([
            {'fieldname': 'seat_no', 'fieldtype': 'Data', 'label': 'Seat Number', 'reqd': 1},
        ],function (values){
            console.log(values);
            frm.set_value('seat',values.seat_no)
        },'Select Seat','Assign')
    },('Actions')); 
}