# dictionary
# key-value pair

person = dict(name = "rishi", age = 25, city = "delhi")
print(person)
person["age"] = 26
print(person)

country = {}
country["name"] = "India"
country["population"] = 1393409038

print(country)
print(f"country name : {country['name']}")

del country["population"]
print(country)

print(f"person (keys): {person.keys()}")
print(f"person (values): {person.values()}")
print(f"person (items): {person.items()}")

person.update(country)
print(f"person after update: {person}")

# get method

age = person["age"]
print(f"age of person: {age}")

gender = person.get("gender", "not specified"   )  # get method is used to get the value of a key, if the key is not present it returns the default value
print(f"gender of person: {gender}")        