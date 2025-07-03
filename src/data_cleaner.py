# src/data_cleaner.py

import pandas as pd

def clean_retail_data(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans the Online Retail dataset and returns a cleaned DataFrame."""
    df_clean = df.copy()

    # Drop rows with missing InvoiceNo or StockCode
    df_clean.dropna(subset=["InvoiceNo", "StockCode", "Description"], inplace=True)

    # Remove rows with negative or zero quantity or price
    df_clean = df_clean[(df_clean["Quantity"] > 0) & (df_clean["UnitPrice"] > 0)]

    # Remove duplicates
    df_clean.drop_duplicates(inplace=True)

    # Convert InvoiceDate to datetime if not already
    if not pd.api.types.is_datetime64_any_dtype(df_clean["InvoiceDate"]):
        df_clean["InvoiceDate"] = pd.to_datetime(df_clean["InvoiceDate"])

    # Standardize text fields
    df_clean["Description"] = df_clean["Description"].str.strip().str.title()

    # Fill or mark missing CustomerID
    df_clean["CustomerID"] = df_clean["CustomerID"].fillna("Unknown")

    print(f"✅ Cleaned dataset: {df_clean.shape[0]:,} rows remain after cleaning.")
    return df_clean
