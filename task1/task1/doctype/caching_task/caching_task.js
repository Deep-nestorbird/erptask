// Copyright (c) 2024, Deep Prakash Srivastava and contributors
// For license information, please see license.txt

// frappe.ui.form.on("caching_task", {
// 	refresh(frm) {

// 	},
// });
frappe.call({
    method: "task1.task1.doctype.caching_task.caching_task.set_cached_items",
    callback: function(response) {
        console.log(response.message);
    }
});

frappe.call({
    method: 'task1.task1.doctype.caching_task.caching_task.get_cached_items',
    callback: function(response) {
        console.log(response.message);
    }
});
