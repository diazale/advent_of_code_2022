f = open("input_day_4.txt", "r")
in_data = f.read()
f.close()

pairs = [p.split(",") for p in in_data.split("\n")]

def min_max(range_):
    # Return the lower and upper bounds of each pair
    r1_, r2_ = range_.split("-")
    return int(r1_), int(r2_)

# Part 1: Given a pair of ranges, does one contain the other fully?
contained_count = 0
for pair in pairs:
    range1 = min_max(pair[0])
    range2 = min_max(pair[1])

    if (min(range1) >= min(range2)) and (max(range1) <= max(range2)) or \
            (min(range2) >= min(range1) and max(range2) <= max(range1)):
        contained_count += 1

    #print(pair, range1, range2)

#print(contained_count)

# Part 2: Given a pair of ranges, is there any overlap at all?
overlap_count = 0
for pair in pairs:
    overlap = False
    range1 = min_max(pair[0])
    range2 = min_max(pair[1])

    if min(range2) <= min(range1) <= max(range2) or \
        min(range1) <= min(range2) <= max(range1):
        overlap = True
        overlap_count += 1

    print(pair, overlap)

print(overlap_count)