import frappe
from frappe.model.document import Document

class caching_task(Document):
    pass

@frappe.whitelist()
def set_cached_items():
    cache_key = "data_list"
    cache = frappe.cache()

    # Example items to cache
    data = [
        {"name": "Deep Prakash"},
    ]
    
    # Store the items in the cache
    cache.set_value(cache_key, data)
    return "Data have been cached."

@frappe.whitelist()
def get_cached_items():
    cache_key = "data_list"
    cache = frappe.cache()
    data = cache.get_value(cache_key)
    return data