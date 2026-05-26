def serve_chai():
    chai_type = "masala"   # local
    print(chai_type)

chai_type = "lemon"
serve_chai()
print(f"outside :", {chai_type})



def chai_counter():
    chai_type = "lemon"

    def print_order():
        chai_type = "ginger"
        print(chai_type)   #---- ginger

    print(chai_type)  # --- lemon
    print_order()  #----- call ginger

chai_type = "masala"
chai_counter()   # ---- call lemon
print(chai_type)  # ---- masala

