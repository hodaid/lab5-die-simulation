import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(42)

# Simulate rolling a fair six-sided die 1000 times
rolls = np.random.randint(1, 7, size=1000)

# (a) Print the first 10 rolls
print("First 10 rolls:", rolls[:10])

# (b) Count occurrences of each face (1-6)
faces, counts = np.unique(rolls, return_counts=True)

# (c) Compute and print empirical and theoretical probabilities
print(f"\n{'Face':<6} {'Count':<7} {'Empirical P':<13} {'Theoretical P'}")
for face, count in zip(faces, counts):
    emp_p = count / 1000
    theo_p = 1 / 6
    print(f"{face:<6} {count:<7} {emp_p:<13.3f} {theo_p:.4f}")

# (d) Plot histogram of the 1000 rolls
plt.figure(figsize=(7, 4))
plt.hist(rolls, bins=np.arange(0.5, 7.5, 1), rwidth=0.8, color="steelblue", edgecolor="black")
plt.title("1000 Six-Sided Die Rolls Simulation")
plt.xlabel("Die Face")
plt.ylabel("Frequency")
plt.xticks(range(1, 7))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save the plot
plt.savefig("die_rolls.png")
print("\nSaved die_rolls.png")