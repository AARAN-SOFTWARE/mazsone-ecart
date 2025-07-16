# Copyright (c) 2025, Aaran Software and contributors
# For license information, please see license.txt
from frappe.model.document import Document
import frappe
import re
from frappe.utils import cstr

# Slug generator for SEO-friendly URLs
def slugify(text):
    text = cstr(text).lower()
    text = re.sub(r'[^\w\s-]', '', text)       # Remove special characters
    text = re.sub(r'[\s_-]+', '-', text)       # Replace spaces/underscores with hyphens
    return text.strip('-')

class Product(Document):
    # Auto-generate slug from item_name
    def autoname(self):
        if not self.slug:
            self.slug = slugify(self.item_name)

    # Return SEO keywords as a list
    def get_keywords_list(self):
        if not self.seo_keywords:
            return []
        return [k.strip() for k in self.seo_keywords.split(',') if k.strip()]

# API Methods 
@frappe.whitelist()
def get_product_category(item_code):
    """Get product details with category breadcrumb"""
    product = frappe.get_doc("Product", {"item_code": item_code})

    if not product.category:
        return {"error": "No category linked to this product."}

    category = frappe.get_doc("Category", product.category)

    breadcrumb = []
    current = category
    while current:
        breadcrumb.insert(0, {
            "id": current.name,
            "name": current.get("category_name") or current.name
        })
        if not current.parent_category:
            break
        current = frappe.get_doc("Category", current.parent_category)

    return {
        "product": {
            "item_name": product.item_name,
            "item_code": product.item_code
        },
        "category": {
            "id": category.name,
            "name": category.get("category_name"),
            "image": category.get("image") or "",
            "breadcrumb": breadcrumb
        }
    }

@frappe.whitelist(allow_guest=True)
def get_product(slug=None, name=None):
    """Get product details by slug or name"""
    if not slug and not name:
        frappe.throw("Please provide either 'slug' or 'name'")

    # Use get_list to fetch document name by slug
    if slug:
        result = frappe.get_list("Product", filters={"slug": slug}, fields=["name"])
        if not result:
            frappe.throw("Product not found for slug: " + slug)
        name = result[0].name

    # Now get full document by name
    product = frappe.get_doc("Product", name)
    doc = product.as_dict()
    doc["seo_keywords_list"] = product.get_keywords_list()

    return doc

@frappe.whitelist(allow_guest=True)
def test_api():
    """Simple test endpoint"""
    return {"message": "API working!"}

 