import frappe
from task1 import LoginManager
from frappe.utils import random_string

class CustomLoginManager(LoginManager):
    def validate_login(self):
        super().validate_login()
        
        # Bypass 2FA for users from restricted IP addresses
        user_ip = frappe.local.request_ip
        restricted_ips = [ip.ip_address for ip in frappe.get_all("IP Whitelist", fields=["ip_address"])]
        
        if user_ip in restricted_ips:
            if frappe.db.get_value("System Settings", None, "bypass_two_factor_auth_for_restricted_ip"):
                return
        
        user = self.user
        if frappe.db.get_value("User", user, "enabled"):
            verification_code = random_string(6)
            frappe.cache().hset("verification_code", user, verification_code)
            self.send_verification_code_via_email(user, verification_code)
            frappe.local.response["verification_needed"] = True

    def send_verification_code_via_email(self, user, verification_code):
        email = frappe.db.get_value("User", user, "email")
        frappe.sendmail(recipients=[email], subject="Your Login Verification Code",
                        message=f"Your verification code is {verification_code}")

def verify_verification_code(user, verification_code):
    stored_code = frappe.cache().hget("verification_code", user)
    return stored_code == verification_code