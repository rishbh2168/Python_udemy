name = ["rishi","rishabh","ravi"]
print(name)

name.append("rishika")
print(name)

name.insert(1,"ayushi")
print(name)

name.remove("rishika")
print(name) 

name.pop()
print(name)

name.reverse()
print(name)

name.sort()
print(name)

numbers = [1, 5, 3, 2, 4]

print(f"maximum number : {max(numbers)}")



# operator overloading

name = ["rishi","rishabh","ravi"]
name2 = ["ayushi","rishika"]

print(name + name2)  # concatenation of two lists

print(name * 3)  # repetition of list

print("rishika" in name)

print("rishika" not in name)

name3 = "rajat"

name4 = bytearray(b"rajat")
print(name3)
print(name4)

name4 = name4.replace(b"ra", b"ri")
print(f"after replace: {name4}")

