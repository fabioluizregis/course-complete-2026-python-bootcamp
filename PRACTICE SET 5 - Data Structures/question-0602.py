products = {
    "Laptop": 999.99,
    "Smartphone": 499.99,
    "Tablet": 299.99,
    "Headphones": 89.99,
    "Smartwatch": 199.99
}
max_price = max(products, key=products.get)
print("The highest priced product costs:", max_price)   

print(f"The highest priced product costs: {products[max_price]} from key {max_price}'")