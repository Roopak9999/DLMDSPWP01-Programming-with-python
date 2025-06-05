# test_vs_ideal_plotter.py

import pandas as pd
import matplotlib.pyplot as plt

def load_csv(file_path):
    return pd.read_csv(file_path)

def get_selected_function_map():
    return {
        "y_test1": "y40",
        "y_test2": "y29",
        "y_test3": "y26",
        "y_test4": "y50"
    }

def plot_test_vs_ideal(test_df, ideal_df, selected_map, save_path="test_vs_ideal_functions_plot.png"):
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    axs = axs.ravel()

    for i, (test_col, ideal_col) in enumerate(selected_map.items()):
        axs[i].plot(ideal_df['x'], ideal_df[ideal_col], label=f"Ideal Function {ideal_col}", color='blue')
        axs[i].scatter(test_df['x'], test_df[test_col], label=f"Test Data {test_col}", color='red', zorder=5)
        axs[i].set_title(f"{test_col} vs {ideal_col}")
        axs[i].set_xlabel("x")
        axs[i].set_ylabel("y")
        axs[i].legend()
        axs[i].grid(True)

    plt.tight_layout()
    plt.suptitle("Figure: Test data points and each selected ideal function", fontsize=16, y=1.03)
    plt.subplots_adjust(top=0.9)
    plt.savefig(save_path, dpi=300)
    plt.close()  # Prevent GUI pop-up in tests

