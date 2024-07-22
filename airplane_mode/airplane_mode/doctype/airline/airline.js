// Copyright (c) 2024, anwarpatelnoori and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airline", {
    refresh(frm) {
        if (frm.doc.website){
            add_website_button(frm);
        }
    },
});
function add_website_button(frm) {
    let url = frm.doc.website;
    const add_comment_button_html = `
                <li class="website">
                    <a href="${url}"target="_self">Visit Webste</a>
                </li>
            `;
    $(add_comment_button_html).insertBefore('.form-sidebar');
    
    // when i click on the Visit Website button, it should open the website in a new tab
    $('.website a').click(function (e) {
        e.preventDefault();
        var url = $(this).attr('href');
        // open the link in same window
        window.location.href = url;
    }
    ); 
}