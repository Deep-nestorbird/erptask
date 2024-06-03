# # Copyright (c) 2024, Deep Prakash Srivastava and Contributors
# # See license.txt

# # import frappe
# from frappe.tests.utils import FrappeTestCase


# class Testtest(FrappeTestCase):
# 	pass
import unittest
from frappe.tests.utils import FrappeTestCase
from .test import test

class TestTest(FrappeTestCase):
    
    def test_document_creation(self):
        # Create a new document instance
        new_doc = test({
            "doctype": "test",
            "name1": "Test Document"
        })
        
        # Save the document
        new_doc.insert()
        
        # Check if the document is inserted
        self.assertIsNotNone(new_doc.name)
        
        # Optionally, you can also check for other assertions, like the value of a field
        self.assertEqual(new_doc.name1, "Test Document")
        
        # Clean up (delete the created document)
        new_doc.delete()

if __name__ == '__main__':
    unittest.main()
