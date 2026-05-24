cup_size = input("Please enter your prefer cup size (small/medium/large) : ").lower()

if cup_size == "small" :
    print(f"{cup_size} cup price = 10$")
elif  cup_size == "medium" :
    print(f"{cup_size} cup price = 20$")
elif cup_size == "large" :
    print(f"{cup_size} cup price = 30$")

else:
    print("unknown cup size")