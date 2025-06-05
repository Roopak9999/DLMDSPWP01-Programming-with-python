# Unit Tests.py

import unittest
import pandas as pd
from test_vs_ideal_plotter import load_csv, get_selected_function_map, plot_test_vs_ideal
import os


class TestPlottingFunctions(unittest.TestCase):

    def test_load_csv(self):
        # Create a simple dummy CSV
        df = pd.DataFrame({'x': [1, 2], 'y_test1': [3, 4]})
        df.to_csv("dummy.csv", index=False)

        loaded_df = load_csv("dummy.csv")
        self.assertListEqual(list(loaded_df.columns), ['x', 'y_test1'])
        os.remove("dummy.csv")

    def test_get_selected_function_map(self):
        mapping = get_selected_function_map()
        self.assertIn("y_test1", mapping)
        self.assertEqual(mapping["y_test1"], "y40")

    def test_plot_saves_file(self):
        # Dummy test/ideal data
        df = pd.DataFrame({'x': [0, 1], 'y_test1': [1, 2], 'y_test2': [2, 3], 'y_test3': [3, 4], 'y_test4': [4, 5]})
        ideal_df = pd.DataFrame({'x': [0, 1], 'y40': [1, 1], 'y29': [2, 2], 'y26': [3, 3], 'y50': [4, 4]})
        mapping = get_selected_function_map()

        plot_test_vs_ideal(df, ideal_df, mapping, save_path="temp_plot.png")
        self.assertTrue(os.path.exists("temp_plot.png"))
        os.remove("temp_plot.png")


if __name__ == '__main__':
    unittest.main(verbosity=2)
