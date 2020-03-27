import re

# Set examples

s = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}

# Remove dupes
dedeuped = set(s)
print(dedeuped)

s.add(6)
print(s)

# Use discard because remove throws if item does not exist.
s.discard(1)
print(s)

copy = s.copy()
print(copy is s)
print(copy == s)

# Set algebra

regex = re.compile(r"[\w]+")
words = set(regex.findall("Once more unto the breach dear friends once more; Or close the wall up with our English "
                          "dead.".lower()))

stop_words = {"the", "or", "our", "unto"}

# Remove stop words from set
cleaned = words.difference(stop_words)
print(cleaned)
print(cleaned is words)
print(cleaned.intersection(stop_words))
print(cleaned.isdisjoint(stop_words))
