import matplotlib.pyplot as plt

# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# First plot
ax1.plot([1, 2, 3], [1, 4, 9], color='blue')
ax1.set_title("Graph 1")

# Second plot
ax2.plot([1, 2, 3], [1, 2, 3], color='green')
ax2.set_title("Graph 2")

# Display the plots
plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()
