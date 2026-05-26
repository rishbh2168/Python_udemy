value = 15
remainder = value / 3

if remainder :
    print("yes it is divisble")
else:
    print(f"{value} is not divisble by 3")

# by walrus operator:

value = 15

if(remainder := value / 3) :
    print("yes")