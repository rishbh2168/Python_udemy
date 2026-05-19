masala = ("spicy", "hot", "sweet")
print(f"masala is: {masala}")

(s1, s2, s3) = masala
print(f"first element of masala is: {s1}")
print(f"second element of masala is: {s2}")
print(f"third element of masala is: {s3}")

ginger, clove = 2,3
print(f"ration of ginger: {ginger} and clove: {clove}")

#swaping values
ginger, clove = clove, ginger
print(f"ration of ginger: {ginger} and clove: {clove}")


#membership operator

print(f" is spicy in masala? {"spicy" in masala}")    # in is used to check if an element is present in the tuple or not