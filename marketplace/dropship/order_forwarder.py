def forward_order_to_supplier(order_data, supplier="gosupps"):
    # Send via email API or automated browser bot
    print(f"Forwarding order to {supplier.upper()} for: {order_data['product_title']}")