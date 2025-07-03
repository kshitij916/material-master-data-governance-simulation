# src/kpi_calculator.py

import pandas as pd

def simulate_material_master(df: pd.DataFrame) -> pd.DataFrame:
    """Creates a simulated material master table from cleaned retail data."""
    materials = df.drop_duplicates(subset=["StockCode", "Description"])[["StockCode", "Description"]].copy()

    materials.rename(columns={
        "StockCode": "MaterialNumber",
        "Description": "MaterialDescription"
    }, inplace=True)

    # Simulate additional fields
    materials["MaterialType"] = materials["MaterialNumber"].apply(lambda x: "FERT" if str(x).startswith("1") else "HALB")
    materials["BaseUnit"] = "EA"  # Default to Each
    materials["ProcurementType"] = "E"  # 'E' = In-house production, 'F' = External
    materials["Plant"] = "1000"
    materials["ValuationClass"] = "3000"

    return materials


def calculate_kpis(materials_df: pd.DataFrame) -> dict:
    """Calculates data quality KPIs for the material master."""
    total = len(materials_df)
    kpis = {
        "Total Materials": total,
        "Missing Descriptions": materials_df["MaterialDescription"].isnull().sum(),
        "Duplicate Material Numbers": materials_df["MaterialNumber"].duplicated().sum(),
        "Unique Material Types": materials_df["MaterialType"].nunique(),
        "Materials with Short Description (<5 chars)": (materials_df["MaterialDescription"].str.len() < 5).sum(),
    }
    kpis["% Missing Descriptions"] = round(kpis["Missing Descriptions"] / total * 100, 2)
    return kpis
