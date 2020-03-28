from pprint import pprint as pp

words = "Four score and seven years ago".split()

# List comprehension
word_lengths = [len(word) for word in words]
print(word_lengths)

# Set comprehension
word_lengths_set = {len(word) for word in words}
print(word_lengths_set)

# Dictionary comprehension
state_to_capital = {"Washington": "Olympia",
                    "Hawaii": "Honolulu",
                    "Oregon": "Salem",
                    "California": "Sacramento"}

pp({state.upper(): capital.upper() for state, capital in state_to_capital.items()})

