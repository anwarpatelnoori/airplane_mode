// Copyright (c) 2024, anwarpatelnoori and contributors
// For license information, please see license.txt
frappe.ui.form.on("Airplane Flight", {
    refresh(frm) {
        change_gate_number(frm);
    },
});

function change_gate_number(frm) {
    if (frm.doc.docstatus == 1) {
        frm.add_custom_button('Change Gate Number', function() {
            frappe.prompt(
                [
                    {
                        fieldname: 'gate',
                        fieldtype: 'Link',
                        options: 'Airport Gate',
                        label: 'New Gate Number',
                        reqd: 1
                    }
                ],
                function(values) {
                    console.log(values);
                    frappe.call({
                        method: 'frappe.client.get_list',
                        args: {
                            doctype: 'Airplane Ticket',
                            filters: {
                                'flight': frm.doc.name
                            },
                            fields: ['name', 'gate_number'] // Specify the fields you want to retrieve
                        },
                        callback: function(response) {
                            if (response.message) {
                                let tickets = response.message;
                                tickets.forEach(function(ticket) {
                                    frm.set_value('gate_number',values.gate),
                                    frappe.call({
                                        method: 'frappe.client.set_value',
                                        args: {
                                            doctype: 'Airplane Ticket',
                                            name: ticket.name,  // Set the ticket's name
                                            fieldname: 'gate_number',
                                            value: values.gate   // Set the new gate number
                                        },
                                        callback: function(response) {
                                            if (!response.exc) {
                                                frappe.msgprint(`Ticket ${ticket.name} updated with gate number ${values.gate}`);
                                            }
                                        }
                                    });
                                });
                            }
                        }
                    });
                },
                'Change Gate Number',
                'Change'
            );
        });
    }
}
