# Material Master Data Simulation Project

This project simulates a basic Material Master Data Management System inspired by real-world SAP environments. It uses the Online Retail dataset to demonstrate:

- Data ingestion and cleaning
- Master data structure simulation
- Data governance rules
- Workflow simulation (request → validation → creation)
- KPI tracking and dashboarding

## 🧰 Tech Stack

- Python (Pandas, Streamlit, Matplotlib)
- Jupyter Notebooks
- Excel (.xlsx dataset)
- BPMN diagram (for visualizing process)

## 📁 Project Structure

See [Project Structure](#project-structure) section above for explanation of directories and files.

## 🚀 Getting Started

1. Clone the repository:
git clone https://github.com/yourusername/material-master-data-simulation.git
cd material-master-data-simulation


2. Create a virtual environment and install dependencies:
pip install -r requirements.txt


3. Upload the `Online Retail.xlsx` dataset to the `data/` folder.

4. Run the Streamlit dashboard:
streamlit run dashboards/streamlit_app.py


## 📊 KPIs Included

- Material data completeness
- Duplicate material detection
- Workflow time analysis
- Top errors by field
- Data quality score

## 🏛️ Data Governance

See `docs/data_governance_policy.md` for defined roles, rules, and processes.

---

