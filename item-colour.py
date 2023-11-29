# def display_product_and_color(items, colors):
#  for item in items:
#    print(item)
#  for colour in  colors:
#    print(colour)


# ここから下は触らないでください
# 利用するデータ
items = [
    {'name': 'Tシャツ', 'type': 'clothes', 'price': 2000},
    {'name': 'キャップ', 'type': 'cap', 'price': 8000}
]
colors = ['Red', 'Blue', 'Black']


for item in items:
   for color in colors:
       print(item["name"] + ":" + color)
   



# item_names = [item["name"]for item in items]
# print(item_names)

# item_names = [item["name"]for item in items]
# print(item_names)

# 関数の呼び出し
# display_product_and_color(items, colors)