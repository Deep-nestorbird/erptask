import frappe
from task1.override_login import verify_verification_code

@frappe.whitelist(allow_guest=True)
def verify_code(user, verification_code):
    if verify_verification_code(user, verification_code):
        frappe.local.login_manager.user = user
        frappe.local.login_manager.post_login()
        frappe.response['message'] = 'Verification successful'
    else:
        frappe.throw('Invalid verification code')