# my_custom_app/auth_utils.py

import random
import string
import frappe

def generate_otp():
    otp = ''.join(random.choices(string.digits, k=6))
    return otp

def send_otp(email, otp):
    subject = "Your OTP for Login"
    message = f"Your OTP is: {otp}"
    frappe.sendmail(recipients=email, subject=subject, message=message)
