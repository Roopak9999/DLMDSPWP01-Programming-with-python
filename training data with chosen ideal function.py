import matplotlib
matplotlib.use("Agg")  # Use a non-interactive backend

import pandas as pd
import matplotlib.pyplot as plt

# Load data
train_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")
ideal_df = pd.read_csv("ideal.csv")

# Map training functions to ideal function matches
training_ideal_map = {
    "y1": "y40",
    "y2": "y29",
    "y3": "y26",
    "y4": "y50"
}

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
axs = axs.ravel()

# For each training function
for i, (train_col, ideal_col) in enumerate(training_ideal_map.items()):
    # Plot ideal function
    axs[i].plot(ideal_df["x"], ideal_df[ideal_col], color="blue", label=f"Ideal Function {ideal_col}")

    # Plot training data
    axs[i].scatter(train_df["x"], train_df[train_col], color="green", label=f"Training Data {train_col}", alpha=0.6)

    # Plot assigned test points (if any)
    test_col = f"y_test{i + 1}"
    if test_col in test_df.columns:
        axs[i].scatter(test_df["x"], test_df[test_col], color="red", label=f"Test Points {test_col}", zorder=5)

    axs[i].set_title(f"{train_col} and Assigned Points vs {ideal_col}")
    axs[i].set_xlabel("x")
    axs[i].set_ylabel("y")
    axs[i].legend()
    axs[i].grid(True)

# Adjust layout
plt.tight_layout()
plt.suptitle("Training Data with Matched Ideal Functions and Assigned Test Points", fontsize=16, y=1.02)
plt.subplots_adjust(top=0.9)
plt.savefig("training_vs_ideal_with_test.png", dpi=300)
# plt.show()  # Skip this since Agg backend is non-interactive
