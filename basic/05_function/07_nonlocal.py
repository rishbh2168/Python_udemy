def update_order():
    chai_type = "masala"

    def kitchen():

        nonlocal chai_type    # --- calling just above function variable means "masala" one not globally only just above it 
        chai_type = "ginger"  #---- update the chai_type fpr kitchen and update_order function

    kitchen()
    print("after update", chai_type)

update_order()

