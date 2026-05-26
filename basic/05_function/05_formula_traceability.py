def vat_calculator(price, vat):
    return price * (100 + vat)/100

order = [100,150,200]

for price in order:
    final_amount = vat_calculator(price,10)
    print(f"original amount is : {price}, after vat amount is : {final_amount}")