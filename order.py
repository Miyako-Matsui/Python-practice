# 対象ユーザーの注文履歴を返す処理を作成してください
# def get_order_history(user, orders):
#   user_orders = []

#   for order in orders:
#     if order["user_id"] == user["user_id"]: 
#       user_orders.append(order)
#   return user_orders

orders = [
    {
        'order_id': 1,
        'user_id': 1,
        'items': [
            {'name': 'キャップ', 'type': 'cap', 'price': 8000},
            {'name': 'Tシャツ', 'type': 'clothes', 'price': 2000}
        ]
    },
    {
        'order_id': 2,
        'user_id': 2,
        'items': [
            {'name': 'ランニングシューズ', 'type': 'shoes', 'price': 15000},
        ]
    },
    {
        'order_id': 3,
        'user_id': 1,
        'items': [
            {'name': 'スポーツドリンク', 'type': 'food', 'price': 150}
        ]
    },
    {
        'order_id': 4,
        'user_id': 3,
        'items': [
            {'name': 'アンダーウェア', 'type': 'clothes', 'price': 4500},
            {'name': 'テニスラケット', 'type': 'sports goods', 'price': 8000}          
        ]
    }
]

user = {'user_id': 1, 'status': 'basic'}



def get_order_history(user, orders):
  user_order = []
  for order in orders:
   if order["user_id"] == user["user_id"]:
     user_order.append(order)
     print("here",order)
     return user_order



# for order in orders:
#    print("order", order) #すべての情報
#    for item in order["items"]:
#       print(item["price"]) #priceのみの情報

# for order in orders:
#     print(order["order_id"]) #order_id の数字のみ1　2　3　4


#only keys　in dictionary
# student = {"name": "john", "age":25, "course":["math","music"]}
# for key in student:
#   print(key)

# for key,value in student.items():
#   print(key,value)



# # 関数の呼び出し
user_orders = get_order_history(user, orders)
for order in user_orders:
    print(order)