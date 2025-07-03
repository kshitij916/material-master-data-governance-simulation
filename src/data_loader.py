# src/data_loader.py

import pandas as pd
import os

def load_retail_data(filepath: str) -> pd.DataFrame:
    """Loads the Online Retail dataset from the given Excel file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found at {filepath}")
    
    df = pd.read_excel(filepath)
    print(f"✅ Loaded dataset with {df.shape[0]:,} rows and {df.shape[1]} columns.")
    return df
