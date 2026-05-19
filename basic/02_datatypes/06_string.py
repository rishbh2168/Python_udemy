chai = "masala chai"
sugar = "two spoons"
print(f"want to drink {chai} with {sugar} of sugar")

print(f" first word of chai is : {chai[0:6]}")
print(f" last word of chai is : {chai[7:]}")
print(f" last word of chai is : {chai[-4:]}")
print(f" jump word of chai is : {chai[0:6:2]}")

print(f" first word of chai is : {chai[: : -1]}") # reverse the string

#encoded and decoded a string

encoded_chai = chai.encode("utf-8")
print(f"encoded chai is: {encoded_chai}")

decoded_chai = encoded_chai.decode("utf-8")
print(f"decoded chai is: {decoded_chai}")
