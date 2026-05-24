order_amount = int(input("Please enter your order amount :"))

delivery_fee = 0 if order_amount > 300 else 30

print(f"your delivery fee : {delivery_fee}")
