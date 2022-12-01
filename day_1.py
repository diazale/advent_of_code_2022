import numpy as np

f = open("input_day_1.txt", "r")
in_data = f.read()
f.close()

calories = [[int(c) for c in i.split("\n")] for i in in_data.split("\n\n")]
calories_per_elf = np.array([np.sum(c) for c in calories])

# Part 1: Find the elf with the most calories. How many do they have?
print(np.max(calories_per_elf))

# Part 2: Find the top three and sum their calories
print(np.sum(calories_per_elf[np.argsort(calories_per_elf)][-3:]))