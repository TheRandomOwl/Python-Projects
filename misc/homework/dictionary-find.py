products = {
    'C200': {'name': 'UIUC Coaster', 'price': 399.99},
    'P1900': {'name': 'Python Mug', 'price': 19.95},
    'A100': {'name': 'AI Notebook', 'price': 29.99},
    'X500': {'name': 'Xamarin Mousepad', 'price': 12.95}
}

# interate through the dictionary and find the name of the product with the price of 19.95
for key in products:
    if products[key]['price'] == 19.95:
        print(products[key]['name'])
        break

products_number = list(products)
product_info = products['P1900']
