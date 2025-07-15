# Copyright (c) 2025, Aaran Software and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe  # Import the Frappe module
import re
from frappe.utils import cstr

def slugify(text):
    text = cstr(text).lower()
    text = re.sub(r'[^\w\s-]', '', text)       # Remove special chars
    text = re.sub(r'[\s_-]+', '-', text)       # Replace space/underscore with dash
    return text.strip('-')

class Product(Document):
    def autoname(self):
        if not self.slug:
            self.slug = slugify(self.item_name)


 