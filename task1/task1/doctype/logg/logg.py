# Copyright (c) 2024, Deep Prakash Srivastava and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


# class logg(Document):
# 	pass
# import frappe
# from frappe.model.document import Document

class logg(Document):
    def error(self):
        try:
            x = 1/0 
            return x
        except ZeroDivisionError as e:
            frappe.log_error(frappe.get_traceback(), 'Error')
            return None
        except Exception as e:         
            frappe.log_error(frappe.get_traceback(), 'Error')    
            return None
