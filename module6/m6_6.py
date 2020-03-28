from itertools import chain

sunday_temps = [68, 75, 72, 80]
monday_temps = [71, 80, 75, 81]
tuesday_temps = [70, 82, 77, 79]

for temps in zip(sunday_temps, monday_temps, tuesday_temps):
    min_temp = min(temps)
    max_temp = max(temps)
    avg_temp = sum(temps) / len(temps)

    print(f"Min: {min_temp}; Max: {max_temp}; Avg: {avg_temp}")

all_temps = chain(sunday_temps, monday_temps, tuesday_temps)

print(all(t > 32 for t in all_temps))
print(any(t == 90 for t in all_temps))
