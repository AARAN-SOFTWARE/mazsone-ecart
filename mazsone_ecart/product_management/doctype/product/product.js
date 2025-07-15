// Copyright (c) 2025, Aaran Software and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Product", {
//     onload: (frm) => {
//       		// should never check Private
//       		frm.fields_dict["image"].df.is_private = 0;
// 	},
// });
// frappe.ui.form.on('Website Item', {
// 	onload: (frm) => {
// 		// should never check Private
// 		frm.fields_dict["website_image"].df.is_private = 0;
// 	},
frappe.ui.form.on('Product', {
  refresh: function(frm) {
      // your logic here
  }
});
