import datetime
import math

formattedString = "SEA-HNL"
origin, _, destination = formattedString.partition("-")
print(f"The origin is {origin} and the destination is {destination}.")

print(f"The current time is {datetime.datetime.now().isoformat()}")

print(f"PI = {math.pi:.5f} and E = {math.e:.5f}")

# Range examples

# Prints 0 - 4
print(", ".join(str(n) for n in range(5)))

# Prints every 3rd number
print(list(range(10, 20, 3)))

# Python way to print list of numbers
s = range(100, 110)
for n in s:
    print(n)


# If you need a counter, use enumerate
s = range(100, 110)
for index, n in enumerate(s):
    print(f"{index, n}")

# Reverse a list. This makes another copy of the list so not the most efficient method.
original = range(1, 10)
changed = original[::-1]
print(list(changed))
print(original is changed)

# Slicing lists
s = range(0, 1001)

# Print items 150 to 200
print(list(s[150: 201]))

# Print everything except the first and next to last items
print(list(s[1:-1]))

# Print the first 5 items
print(list(s[:5]))

# Print the last 5 items
print(list(s[996:]))

# Copy a list
copy = s[:]
print(len(copy))
print(copy is s)
print(copy == s)

# Sort a list of words by length of the word in descending order
words = "Four score and seven years ago".split()
words.sort(key=len, reverse=True)
print(words)

# Side-effect free sorting
x = [2, 10, 1, -19, 8]
y = sorted(x)
print(y)
print(x is y)

# Side-effect free reversing
z = list(reversed(x))
print(z)
print(z is x)

