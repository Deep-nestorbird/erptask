# # Import necessary modules
# import frappe
# from frappe.model.document import Document
# from frappe.utils.password import encrypt, decrypt

# class Adhaar_details(Document):
#     def before_save(self):
#         # Check if the aadhar card field is not encrypted
#         if not self.get("__encrypted") or "adhaar_number" in self.get("__unsaved"):
#             # Encrypt the aadhar card field using a Frappe method
#             self.adhaar_number = encrypt(self.adhaar_number)
#     @frappe.whitelist(allow_guest=True)
#     def validate_adhaar(adhaar_number):
#     # Assuming you have a custom class/method to validate Aadhaar number
#      is_valid = Adhaar_details.validate_adhaar(adhaar_number)
#      return {"is_valid": is_valid}
#     # def on_update(self):
#     #     # Ensure that the field is marked as encrypted after encryption
#     #     if not self.get("__encrypted"):
#     #         self.set("__encrypted", True)

#     # def on_submit(self):
#     #     # Prevent re-encryption on subsequent submissions
#     #     if not self.get("__unsaved"):
#     #         self.adhaar_number = decrypt(self.adhaar_number)
import frappe
from frappe.model.document import Document
from frappe.utils.password import encrypt

class Adhaar_details(Document):
    def before_save(self):
        # Check if the Aadhaar number field is not encrypted
        if not self.get("__encrypted") or "adhaar_number" in self.get("__unsaved"):
            # Encrypt the Aadhaar number field using Frappe's encryption method
            self.adhaar_number = encrypt(self.adhaar_number)

    @frappe.whitelist(allow_guest=True)
    def validate_adhaar(self, adhaar_number):
        # Assuming you have a custom method to validate Aadhaar numbers
        is_valid = self.validate_adhaar_number(adhaar_number)
        return {"is_valid": is_valid}
@frappe.whitelist(allow_guest=True)
def validate_adhaar_number(self, adhaar_number):
    # Implement your Aadhaar number validation logic here
    # For example, you could check the length or use regex to validate the format
    # This is just a placeholder, you should replace it with your actual validation logic
    if len(adhaar_number) == 12:
        return True
    else:
        return False
