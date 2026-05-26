#chai_type = "masala chai"

#def prepare(order):
#    print("prepare",order)

#prepare(chai_type)
#print(chai_type)

cup = [1,2,3]

def order(chai):
    chai[1]=40
    print("update", cup)

order(cup)
print(cup)


def make_chai(tea,milk,sugar):

    print(tea,milk,sugar)

make_chai("assam", "yes", "no")  # positional argument : we remember place of parameter
make_chai(tea="kerala", sugar="yes", milk="no")  # keywords argument  : we didnot remember place of param



def sp_chai(*ingrident, **extra):

    print("Ingrident", ingrident)
    print("Extra", extra)

sp_chai("ginger", "lemon", sugar="yes", milk="no")
