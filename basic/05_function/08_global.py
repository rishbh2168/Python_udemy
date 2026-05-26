chau_type = "lemon"

def update_order():
    chai_type = "masala"
    def kitchen():

        global chai_type    # --- calling global varibale and update it not above one global one
        chai_type = "ginger"  #---- update the chai_type for global

    kitchen()
    print("after update", chai_type)  #---- this print masala only because no update

update_order()
print(chai_type)
