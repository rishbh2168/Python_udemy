def local_chai():
    yield "masala chai"

def imported_chai():
    yield "matcha"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)


 