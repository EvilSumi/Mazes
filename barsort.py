import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            yield arr

# Generate random data
np.random.seed(42)
data = np.random.randint(1, 101, 20)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(range(len(data)), data, align="edge", width=0.8)
ax.set_xlim(0, len(data))
ax.set_ylim(0, max(data) * 1.1)
ax.set_title("Bubble Sort Visualization")
text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

# Animation update function
def update(frame):
    for rect, val in zip(bars, frame):
        rect.set_height(val)
    text.set_text(f"Number of operations: {next(counter)}")
    return bars + [text]

# Initialize counter
counter = iter(range(1, 1000000))

# Create the animation
anim = FuncAnimation(fig, update, frames=bubble_sort(data),
                     blit=True, interval=50, repeat=False)

plt.show()