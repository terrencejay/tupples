def unpack():
    order = [
        ("Alice", "Laptop", 1),
        ("Bob", "Camera", 2),
        #more orders
    ]
    for customer, product, quantity in order:
        print(f"Customer: {customer}, Product: {product}, Quantity: {quantity}")

unpack()