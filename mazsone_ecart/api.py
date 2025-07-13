import frappe

def set_cors_headers():
    allowed_origins = [
        "http://localhost:5173",
        "https://techmedia-beta.vercel.app/"       # example domain 2
    ]

    origin = frappe.get_request_header("Origin")
    if origin and origin in allowed_origins:
        headers = frappe.local.response.setdefault("headers", {})
        headers["Access-Control-Allow-Origin"] = origin
        headers["Access-Control-Allow-Credentials"] = "true"
        headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, PUT, DELETE"
        headers["Access-Control-Allow-Headers"] = (
            "Content-Type, Authorization, X-Frappe-CSRF-Token"
        )
