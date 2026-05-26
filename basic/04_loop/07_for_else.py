staff = [("a", 15), ("b", 16), ("c", 17)]

for name,age in staff:
    if age <= 18:
        print(f"{name} is eligible to work")
        break

else:
    print(f"{name} not eligible")