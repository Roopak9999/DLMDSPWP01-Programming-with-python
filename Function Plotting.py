import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend to avoid Tkinter error

import pandas as pd
import matplotlib.pyplot as plt

# Load data
train_df = pd.read_csv("Python/train.csv")
ideal_df = pd.read_csv("Python/ideal.csv")

# Define the comparison pairs
comparisons = [
    ('y1', 'y21'),
    ('y1', 'y23')
]

# Create the plot
fig, axs = plt.subplots(1, 2, figsize=(10, 4))  # 1 row, 2 columns
axs = axs.ravel()  # Flatten the axes array

for i, (train_col, ideal_col) in enumerate(comparisons):
    axs[i].plot(train_df['x'], train_df[train_col], 'o', color='green', label='1st training function', markersize=4)
    axs[i].plot(ideal_df['x'], ideal_df[ideal_col], '-', color='orange', linewidth=6, label=f'{ideal_col} ideal function')
    axs[i].legend()
    axs[i].set_xticks([])
    axs[i].set_yticks([])
    axs[i].set_facecolor('white')

fig.patch.set_facecolor('black')  # Match example background
plt.tight_layout()
plt.savefig("function_comparison_plot.png", dpi=300)
print("Plot saved as function_comparison_plot.png")
