name = ["A", "b","c","discontinue"]


for name in name:
    if name == "b":
        continue
    if name == "discontinue":
        print(f"{name} appear")
        break
    print(f"{name} appear")

print("done")