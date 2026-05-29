def chai():
    print("welcome to store!")
    order = yield

    while True:
        print("prepare :", order)
        order = yield

stall = chai()
next(stall)  # start generatoe

stall.send("masala chai")
stall.send("lemon chai")