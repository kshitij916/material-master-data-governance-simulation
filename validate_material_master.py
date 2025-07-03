import pandas as pd

# Load raw dataset
df = pd.read_csv('../data/material_master_raw.csv')

# Define valid values
valid_units = ['pcs', 'kg', 'l']
valid_statuses = ['Draft', 'Approved', 'Rejected']

# Track issues
issues = []

# Check for duplicate MaterialNumber
duplicates = df[df.duplicated(subset=['MaterialNumber'], keep=False)]
if not duplicates.empty:
    issues.append(f'Duplicate MaterialNumbers found: {duplicates["MaterialNumber"].unique().tolist()}')

# Check for missing MaterialName
missing_name = df[df['MaterialName'].isnull() | (df['MaterialName'].str.strip() == '')]
if not missing_name.empty:
    issues.append(f'Missing MaterialNames in rows: {missing_name.index.tolist()}')

# Check for invalid BaseUnit
invalid_units = df[~df['BaseUnit'].isin(valid_units)]
if not invalid_units.empty:
    issues.append(f'Invalid BaseUnits in rows: {invalid_units.index.tolist()}')

# Check for missing Vendor
missing_vendor = df[df['Vendor'].isnull() | (df['Vendor'].str.strip() == '')]
if not missing_vendor.empty:
    issues.append(f'Missing Vendor in rows: {missing_vendor.index.tolist()}')

# Check for invalid Status
invalid_status = df[~df['Status'].isin(valid_statuses)]
if not invalid_status.empty:
    issues.append(f'Invalid Status values in rows: {invalid_status.index.tolist()}')

# Check for non-positive prices
invalid_price = df[df['Price'] <= 0]
if not invalid_price.empty:
    issues.append(f'Invalid Prices (<=0) in rows: {invalid_price.index.tolist()}')

# Output results
if issues:
    print("⚠️  Data validation issues found:")
    for issue in issues:
        print(" -", issue)
else:
    print("All records passed validation checks.")
