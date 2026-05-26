def pure_chai(cups):   #--- pure function
    return cups*10


total_chai = 10

def impure_chai(cups):   #-- impure function --- not recommended
    global total_chai
    total_chai += cups


def pour_chai(n):
    if n == 0:
        return "all cup poured"
    return pour_chai(n-1)

print(pour_chai(3))


chai_types = ["kadak","light","kadak","ginger"]

strong_chai = list(filter(lambda chai: chai=="kadak", chai_types))

print(strong_chai)

    