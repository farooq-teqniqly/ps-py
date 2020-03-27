# Dictionary examples

vehicles = {"Ford": "Mustang", "Mercedes": "GLA250", "BMW": "535i", "BMW": "535i"}

for key, value in vehicles.items():
    print(f"{key}, {value}")

t = [(1, 2), (3, 4), (5, 6)]
print(dict(t))

t = dict(redmond=98052)
print(t)

# Copy dictionary

copy = t.copy()
print(copy is t)
print(copy == t)

copy = dict(t)
print(copy is t)
print(copy == t)

# Append to a dictionary
t.update(dict(bellevue=98008))
print(t)

# Update a dictionary entry
t.update(bellevue=98007)
print(t)

# Check for key existence
print("kent" not in t)
print("redmond" in t)

# Delete item
del t["redmond"]
print(t)

