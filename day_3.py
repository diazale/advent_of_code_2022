# Two rucksacks stored in each row
# First half of the string is rucksack 1, second is rucksack 2

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

# Find the item that appears in both rucksacks
def priority(c):
    # Return the priority of each letter
    # Define it via the unicode value
    if c==c.upper():
        return ord(c) - 38
    else:
        return ord(c) - 96

f = open("input_day_3.txt", "r")
in_data = f.read()
f.close()

rucksacks = in_data.split("\n")

# Part 1: Find the sum of priorities
priorities = 0

for r in rucksacks:
    r1, r2 = r[:len(r)//2], r[len(r)//2:]
    dupe = list(set(r1).intersection((set(r2))))[0]
    priorities += priority(dupe)

print(priorities)

# Part 2: Every 3 lines correspond to an elf group
# Find the item in common each group of 3 and sum their priorities

priorities = 0
for r in range(0,len(rucksacks),3):
    dupe = list(set(rucksacks[r]).intersection(set(rucksacks[r+1])).intersection(set(rucksacks[r+2])))[0]
    priorities += priority(dupe)

print(priorities)