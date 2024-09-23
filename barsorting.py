
import numpy as np
import matplotlib.pyplot as plt

def simple_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        yield arr

# Generate random data
np.random.seed(42)
data = np.random.randint(1, 100, 20)

# Create subplots for before and after sorting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot original data
ax1.bar(range(len(data)), data)
ax1.set_title("Before Sorting")
ax1.set_xlabel("Index")
ax1.set_ylabel("Value")

# Sort the data and get the final sorted array
sorted_data = list(simple_sort(data.copy()))[-1]

# Plot sorted data
ax2.bar(range(len(sorted_data)), sorted_data)
ax2.set_title("After Sorting")
ax2.set_xlabel("Index")
ax2.set_ylabel("Value")

plt.tight_layout()
plt.show()