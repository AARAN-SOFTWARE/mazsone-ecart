import frappe

@frappe.whitelist()
def get_product_category_details(item_code):
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
