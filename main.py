# main.py
import pandas as pd
import numpy as np
from sqlalchemy import create_engine, Column, Integer, Float, String, MetaData, Table
from sqlalchemy.orm import declarative_base, sessionmaker
from bokeh.plotting import figure, show, output_file
import os

Base = declarative_base()

# -----------------------------
# DATABASE TABLE DEFINITIONS
# -----------------------------
class TrainingData(Base):
    __tablename__ = 'training_data'
    id = Column(Integer, primary_key=True)
    x = Column(Float)
    y1 = Column(Float)
    y2 = Column(Float)
    y3 = Column(Float)
    y4 = Column(Float)

class IdealFunctions(Base):
    __tablename__ = 'ideal_functions'
    id = Column(Integer, primary_key=True)
    x = Column(Float)
    # y1 to y50 will be added dynamically later

class TestResults(Base):
    __tablename__ = 'test_results'
    id = Column(Integer, primary_key=True)
    x = Column(Float)
    y = Column(Float)
    ideal_function = Column(String)
    deviation = Column(Float)

# -----------------------------
# EXCEPTION CLASSES
# -----------------------------
class DataLoadError(Exception):
    pass

class FunctionMappingError(Exception):
    pass

# -----------------------------
# DATABASE HANDLER CLASS
# -----------------------------
class DatabaseHandler:
    def __init__(self, db_name='functions.db'):
        self.engine = create_engine(f'sqlite:///{db_name}')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def insert_dataframe(self, df, table_name):
        df.to_sql(table_name, self.engine, if_exists='replace', index=False)

# -----------------------------
# FUNCTION MATCHING LOGIC
# -----------------------------
class FunctionMatcher:
    def __init__(self, train_df, ideal_df):
        self.train_df = train_df
        self.ideal_df = ideal_df

    def find_best_ideal_functions(self):
        matches = {}
        for col in ['y1', 'y2', 'y3', 'y4']:
            min_deviation = float('inf')
            best_function = None
            for ideal_col in self.ideal_df.columns[1:]:
                deviation = np.max(np.abs(self.train_df[col] - self.ideal_df[ideal_col]))
                if deviation < min_deviation:
                    min_deviation = deviation
                    best_function = ideal_col
            matches[col] = best_function
        return matches

    def map_test_data(self, test_df, best_funcs):
        result_rows = []
        for _, row in test_df.iterrows():
            x, y = row['x'], row['y']
            for train_col, ideal_col in best_funcs.items():
                ideal_y = self.ideal_df[self.ideal_df['x'] == x][ideal_col].values
                if len(ideal_y) == 0:
                    continue
                deviation = abs(y - ideal_y[0])
                max_dev = np.max(np.abs(self.train_df[train_col] - self.ideal_df[ideal_col]))
                if deviation <= max_dev * np.sqrt(2):
                    result_rows.append({'x': x, 'y': y, 'ideal_function': ideal_col, 'deviation': deviation})
                    break
        return pd.DataFrame(result_rows)

# -----------------------------
# VISUALIZATION
# -----------------------------
def visualize(train_df, ideal_df, test_df):
    output_file("visualization.html")
    p = figure(title="Training vs Ideal Functions", x_axis_label='x', y_axis_label='y')
    colors = ['red', 'green', 'blue', 'orange']
    for idx, y in enumerate(['y1', 'y2', 'y3', 'y4']):
        p.line(train_df['x'], train_df[y], legend_label=f"train {y}", color=colors[idx], line_width=2)
        p.line(ideal_df['x'], ideal_df[best_funcs[y]], legend_label=f"ideal {best_funcs[y]}", color=colors[idx], line_dash='dashed')
    p.circle(test_df['x'], test_df['y'], size=5, color="black", alpha=0.5, legend_label="Test Data")
    show(p)

# -----------------------------
# MAIN PROGRAM FLOW
# -----------------------------
if __name__ == '__main__':
    db = DatabaseHandler()

    try:
        train_df = pd.read_csv('train.csv')
        ideal_df = pd.read_csv('ideal.csv')
        test_df = pd.read_csv('test.csv')
    except Exception as e:
        raise DataLoadError(f"Error loading CSV files: {e}")

    db.insert_dataframe(train_df, 'training_data')
    db.insert_dataframe(ideal_df, 'ideal_functions')

    matcher = FunctionMatcher(train_df, ideal_df)
    best_funcs = matcher.find_best_ideal_functions()

    mapped_df = matcher.map_test_data(test_df, best_funcs)
    db.insert_dataframe(mapped_df, 'test_results')

    visualize(train_df, ideal_df, mapped_df)
    print("Processing complete. Visualization saved as HTML.")
