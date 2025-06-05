import matplotlib
matplotlib.use('Agg')  # Use backend that does not require Tkinter

import pandas as pd
import matplotlib.pyplot as plt

# Load training data
train_df = pd.read_csv("train.csv")

# Define subplot layout
fig, axs = plt.subplots(2, 2, figsize=(10, 6))
fig.suptitle('Training Data Plots', fontsize=14)

# Function names
columns = ['y1', 'y2', 'y3', 'y4']

# Plot each function in its own subplot
for i, ax in enumerate(axs.flat):
    ax.plot(train_df['x'], train_df[columns[i]], 'r.')  # 'r.' for red dots
    ax.set_title(columns[i])
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_facecolor('white')

# Style the overall figure
plt.subplots_adjust(hspace=0.3, wspace=0.3)
fig.patch.set_facecolor('black')  # Match your image's background

# Save plot instead of displaying it
plt.savefig("train_plot.png", dpi=300)
print("Plot saved as train_plot.png")
