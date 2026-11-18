import numpy as np

source = np.array([100, 200, 300, 400, 500])
target = np.array([100, 210, 300, 400, 480])

# 1. How many values MATCH?
matches = (source == target).sum()

# 2. How many values DIFFER?
differs = (source != target).sum()

# 3. At which POSITIONS do they differ?
positions = np.where(source != target)[0]

print("Matches:", matches)
print("Differs:", differs)
print("Diff positions:", positions)