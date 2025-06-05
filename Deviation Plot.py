import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load training and ideal datasets
train_df = pd.read_csv("train.csv")
ideal_df = pd.read_csv("ideal.csv")

# Define the best-matching ideal functions for each training function
mapping = {
    'y1': 'y40',
    'y2': 'y29',
    'y3': 'y26',
    'y4': 'y50'
}

# Prepare plot
fig, axs = plt.subplots(2, 2, figsize=(10, 6))
fig.patch.set_facecolor('black')  # Black background for figure
axs = axs.ravel()  # Flatten to simplify indexing

for i, (train_col, ideal_col) in enumerate(mapping.items()):
    deviation = np.abs(train_df[train_col] - ideal_df[ideal_col])
    axs[i].fill_between(train_df['x'], 0, deviation, color='skyblue')
    axs[i].set_xticks([])
    axs[i].set_yticks([])
    axs[i].set_facecolor('white')
    axs[i].set_title(f'Deviation: {train_col} vs {ideal_col}', fontsize=10)

plt.tight_layout()

# Save the figure instead of displaying it
plt.savefig("deviation_plot.png", dpi=300)
print("Deviation plot saved as deviation_plot.png")
