daily_sale = [10,20,30,40,10,5,6,7,1,2,3,1,2,3]

total = sum(sale for sale in daily_sale if sale>5)

print(total)