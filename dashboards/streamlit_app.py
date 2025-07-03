# dashboards/streamlit_app.py

import streamlit as st
import pandas as pd
import os
import sys

# Add root directory to import from src/
sys.path.append(os.path.abspath(".."))

from src.kpi_calculator import calculate_kpis

# --- Page Config ---
st.set_page_config(page_title="Material Master Dashboard", layout="wide")

# --- Title ---
st.title("📦 Material Master Data Dashboard")

# --- Load Data ---
data_path = "../data/simulated_material_master.csv"

if not os.path.exists(data_path):
    st.error("Material Master data not found. Please run KPI notebook first.")
    st.stop()

df = pd.read_csv(data_path)

# --- Show Data ---
st.subheader("📋 Simulated Material Master Table")
st.dataframe(df.head(100))

# --- KPI Section ---
st.subheader("📊 Data Quality KPIs")
kpis = calculate_kpis(df)

col1, col2, col3 = st.columns(3)
col4, col5 = st.columns(2)

col1.metric("Total Materials", kpis["Total Materials"])
col2.metric("Missing Descriptions", kpis["Missing Descriptions"])
col3.metric("Duplicate Material Numbers", kpis["Duplicate Material Numbers"])
col4.metric("Short Descriptions", kpis["Materials with Short Description (<5 chars)"])
col5.metric("Unique Material Types", kpis["Unique Material Types"])

st.info(f"📉 % Missing Descriptions: {kpis['% Missing Descriptions']}%")

# --- Filters ---
st.subheader("🔍 Filter by Material Type")
material_types = df["MaterialType"].unique().tolist()
selected_type = st.selectbox("Select a Material Type", options=material_types)

filtered = df[df["MaterialType"] == selected_type]
st.write(f"Showing {len(filtered)} materials of type {selected_type}")
st.dataframe(filtered)

# --- Footer ---
st.markdown("---")
st.caption("Developed for Master Data & Process Architect Role Simulation 🌐")
