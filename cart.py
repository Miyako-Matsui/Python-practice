def calculate_total_with_tax(cart_items,tax_rate):
  prices = [item["price"] for item in cart_items]
  total_price = sum(prices)
  tota_with_tax = total_price * (1 + tax_rate)
  return round(tota_with_tax)


cart_items = [
    {'name': 'Tシャツ', 'type': 'clothes', 'price': 2000},
    {'name': 'キャップ', 'type': 'cap', 'price': 8000}
]

tax_rate = 0.1

total_with_tax = calculate_total_with_tax(cart_items, tax_rate)
print(total_with_tax)


# for item in cart_items:
#   for key, value in item.items():
#     print(key, value)

# prices = [item["price"] for item in cart_items]
# print(sum(prices))

# total_prices = 0 
# for price in prices:
#    total_prices += price
# print(total_prices)