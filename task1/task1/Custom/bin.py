import frappe

# function to retrieve data
def get_stock_data_by_bin(bin_id): 
    try:
        bin_data = frappe.get_list(
            'Bin',
            filters={'name': bin_id},
            fields=['item_code', 'warehouse', 'actual_qty', 'projected_qty', 'reserved_qty']
        )
        return bin_data

    except Exception as e:
        return str(e)

bin_id = 'uf9frc5rai'  
stock_data = get_stock_data_by_bin(bin_id)
print(stock_data)