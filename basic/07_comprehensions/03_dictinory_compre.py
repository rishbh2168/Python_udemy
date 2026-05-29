tea_price_inr = {
    "masala chai" : 40,
    "iced tea" : 100,
    "lemon ginger tea" : 150,
}

tea_price_usd = {tea: price/80 for tea,price in tea_price_inr.items()}
print(tea_price_usd)