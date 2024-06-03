# Copyright (c) 2024, Deep Prakash Srivastava and contributors
# For license information, please see license.txt

# import frappe
# my_custom_app/doctype/auoth2/auoth2.py

import frappe
from frappe.model.document import Document
from task1.auth_utils import generate_otp, send_otp

class auoth2(Document):
    pass

@frappe.whitelist()
def enable_2fa(user_email):
    otp = generate_otp()
    doc = frappe.get_doc({
        "doctype": "auoth2",
        "user": user_email,
        "otp": otp,
        "enabled": 1
    })
    doc.insert(ignore_permissions=True)
    send_otp(user_email, otp)
