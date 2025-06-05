import pandas as pd
import matplotlib.pyplot as plt

# Load test and ideal datasets
test_df = pd.read_csv("C:/Users/Shreya Halder/Downloads/Python/Python/test.csv")
ideal_df = pd.read_csv("C:/Users/Shreya Halder/Downloads/Python/Python/ideal.csv")

# Mapping test data columns to corresponding ideal function columns
selected_ideal_map = {
    "y_test1": "y40",
    "y_test2": "y29",
    "y_test3": "y26",
    "y_test4": "y50"
}

# Create 2x2 subplot layout
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
axs = axs.ravel()  # flatten axes array

# Plot each test column against its matched ideal function
for i, (test_col, ideal_col) in enumerate(selected_ideal_map.items()):
    axs[i].plot(ideal_df['x'], ideal_df[ideal_col], label=f"Ideal Function {ideal_col}", color='blue')
    axs[i].scatter(test_df['x'], test_df[test_col], label=f"Test Data {test_col}", color='red', zorder=5)
    axs[i].set_title(f"{test_col} vs {ideal_col}")
    axs[i].set_xlabel("x")
    axs[i].set_ylabel("y")
    axs[i].legend()
    axs[i].grid(True)

# Adjust layout and add a main title
plt.tight_layout()
plt.suptitle("Figure: Test data points and each selected ideal function", fontsize=16, y=1.03)
plt.subplots_adjust(top=0.9)
plt.savefig("test_vs_ideal_functions_plot.png", dpi=300)
plt.show()

