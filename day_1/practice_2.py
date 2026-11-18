import numpy as ny

arr=ny.random.randint(1,100,1000)
#4
print(arr.mean())
print(arr.min())
print(arr.max())

#3
# Method 1: unique + count
total = len(arr)
unique = len(ny.unique(arr))
print("Duplicate rows:", total - unique)   # extra copies beyond first

# Method 2: see WHICH values repeat and how often
values, counts = ny.unique(arr, return_counts=True)
dupes = values[counts > 1]
print("Duplicate values:", dupes)
print("Their counts:", counts[counts > 1])

# Count values > 50  — ONE line
count_gt_50 = (arr > 50).sum()
print("Values > 50:", count_gt_50)

# Why it works:
#   arr > 50        ->  array of True/False
#   .sum() on bools ->  counts the True's (True=1, False=0)