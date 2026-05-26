def make_chai():

    return "here is you chai"

ret_value = make_chai()

print(ret_value)

def chai():
    pass

print(chai())   #--- none because no return value


def tea(cup_left):
    if cup_left == 0:
        return "sorry no chai"

    return "here is your chai"
    print("hello")  #-- it will not run  --- it will over pass because function already return value
print(tea(0))
print(tea(10))


def tea_owner():
    return 10,20

sold , remaining = tea_owner()

print("sold", sold)
print("remaining", remaining)
