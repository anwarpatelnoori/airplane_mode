import frappe
from frappe.model.document import Document
import random

class AirplaneTicket(Document):
    def before_save(self):
        amount = 0
        if self.add_ons:
            for item in self.add_ons:
                amount += item.amount
            self.total_amount = amount + self.flight_price
        else:
            self.total_amount = self.flight_price

    def validate(self):
        # Remove duplicate add-ons
        unique_add_ons = []
        seen_add_ons = set()
        
        for item in self.add_ons:
            add_ons_item = (item.item)  # Assuming item and amount uniquely identify an add-on
            if add_ons_item not in seen_add_ons:
                seen_add_ons.add(add_ons_item)
                unique_add_ons.append(item)
        
        # Update the add_ons list with unique items
        self.add_ons = unique_add_ons
    def before_submit(self):
         if self.status != "Boarded":
               frappe.throw("You can only submit a ticket if the status is Boarded")
    def before_insert(self):
        random_int = random.randint(1, 100)
        string = 'ABCDE'
        random_string = random.choice(string)
        seat_number = str(random_int) + random_string
        self.seat = seat_number	
    
