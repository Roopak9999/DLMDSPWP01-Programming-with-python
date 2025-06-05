import pandas as pd
import matplotlib.pyplot as plt


def load_csv(filepath):
    """
    Loads a CSV file and returns a pandas DataFrame.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.
    """
    return pd.read_csv(filepath)


def get_selected_function_map():
    """
    Returns a dictionary mapping each test function to its corresponding ideal function.

    Returns:
        dict: Mapping from test function names to ideal function names.
    """
    return {
        "y_test1": "y40",
        "y_test2": "y29",
        "y_test3": "y26",
        "y_test4": "y50"
    }


def plot_test_vs_ideal(test_df, ideal_df, mapping, save_path="test_vs_ideal_plot.png"):
    """
    Plots test data vs. their corresponding ideal functions and saves the plot as a PNG file.

    Args:
        test_df (pd.DataFrame): DataFrame containing test data.
        ideal_df (pd.DataFrame): DataFrame containing ideal function values.
        mapping (dict): Dictionary mapping test function names to ideal function names.
        save_path (str): File path to save the generated plot.
    """
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    axs = axs.ravel()

    for i, (test_col, ideal_col) in enumerate(mapping.items()):
        axs[i].plot(ideal_df['x'], ideal_df[ideal_col], label=f"Ideal: {ideal_col}", color='blue', linewidth=2)
        axs[i].scatter(test_df['x'], test_df[test_col], label=f"Test: {test_col}", color='red', s=25)
        axs[i].set_title(f"{test_col} vs {ideal_col}")
        axs[i].set_xlabel("x")
        axs[i].set_ylabel("y")
        axs[i].legend()
        axs[i].grid(True)

    plt.tight_layout()
    plt.suptitle("Test Data vs Corresponding Ideal Functions", fontsize=16, y=1.02)
    plt.subplots_adjust(top=0.9)
    plt.savefig(save_path, dpi=300)
    plt.close()
