fav_chai = ["masala chai","iced tea","ginger tea","masala chai","iced tea"]

unique_chai = {chai for chai in fav_chai if len(chai) > 10}
print(unique_chai)



recipe = {
    "masala chai" : ["ginger","milk","sugar"],
    "elachi chai" : ["milk", "elachi"],
    "spicy chai" : ["milk", "ginger","black pepper"],

}

unique_spice = {spice for ingredi in recipe.values() for spice in ingredi}

print(unique_spice)