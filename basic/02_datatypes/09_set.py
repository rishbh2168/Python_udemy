classA = {"rishi", "rishabh", "ravi"}
classB = {"ayushi", "rishika", "rishabh"}

print(f"all studenet in both class: {set(classA) | set(classB)}")  # union of two sets

both_class = classA | classB  # union of two sets using operator overloading
print(f"all studenet in both class: {both_class}")  # union of two sets using operator overloading
print(f"students in classA but not in classB: {set(classA) - set(classB)}")  # difference of two sets

print(f"students in both classA and classB: {set(classA) & set(classB)}")  # intersection of two sets

# membership test

print(f" is rishi in class A? {"rishi" in classA}")