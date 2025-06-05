import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend to avoid Tkinter errors

import pandas as pd
import matplotlib.pyplot as plt

# Load test data
test_df = pd.read_csv('test.csv')

# Plot test data
plt.figure(figsize=(10, 6))
plt.plot(test_df['x'], test_df['y'], 'c.', markersize=6)  # 'c.' = cyan dots

# Style to match the example
plt.title("Test Data Points")
plt.xticks([])
plt.yticks([])
plt.grid(False)
plt.gca().set_facecolor('white')         # Plot background
plt.gcf().patch.set_facecolor('black')   # Outer figure background
plt.tight_layout()

# Save plot instead of displaying it
plt.savefig("test_plot.png", dpi=300)
print("Plot saved as test_plot.png")
