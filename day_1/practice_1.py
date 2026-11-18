import numpy as np

# 1. Create an array
arr = np.array([10, 20, 30, 40, 50])

# 2. Vectorized math (no loops!)
print(arr * 2)        # [20 40 60 80 100]
print(arr.sum())      # 150
print(arr.mean())     # 30.0

# 3. Boolean masks (super useful for validation)
print(arr > 25)              # [False False True True True]
print(arr[arr > 25])         # [30 40 50]

# 4. Nulls (very important in ETL)
arr2 = np.array([1.0, np.nan, 3.0])
print(np.isnan(arr2))        # [False True False]

# 5. Comparison — spot differences fast
source = np.array([100, 200, 300])
target = np.array([100, 250, 300])
print(source == target)      # [True False True]
print(np.where(source != target))  # mismatched positions