import matplotlib
matplotlib.use('Agg')  # Use backend that doesn't require a display

import pandas as pd
import matplotlib.pyplot as plt

# Load training and ideal data
train_df = pd.read_csv("train.csv")
ideal_df = pd.read_csv("ideal.csv")

# Map of training function to chosen ideal function
mapping = {
    'y1': 'y40',
    'y2': 'y29',
    'y3': 'y26',
    'y4': 'y50'
}

# Plot each training function with its matched ideal function
fig, axs = plt.subplots(4, 1, figsize=(8, 12))
fig.patch.set_facecolor('black')  # Black background for entire figure

for idx, (train_col, ideal_col) in enumerate(mapping.items()):
    ax = axs[idx]
    ax.plot(ideal_df['x'], ideal_df[ideal_col], 'b-', label=f'Ideal: {ideal_col}')
    ax.plot(train_df['x'], train_df[train_col], 'ro', label=f'Training: {train_col}')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.legend()
    ax.set_facecolor('white')

plt.tight_layout()

# Save plot to file instead of showing
plt.savefig("training_vs_ideal.png", dpi=300)
print("Plot saved as training_vs_ideal.png")
