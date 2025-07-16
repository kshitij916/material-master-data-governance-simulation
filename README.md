# 📦 Material Master Data Governance Simulation

This project simulates an end-to-end **Material Master Data Management System** using the Online Retail dataset (UCI ML Repo). It models how enterprises manage material requests, approvals, audit trails, data governance policies, and quality KPIs — similar to SAP ERP workflows.

---

## 🧩 Core Features

✅ Clean and standardize raw transactional data  
✅ Simulate a material master with essential attributes  
✅ Request → Approve → Create material workflow  
✅ Maintain audit trail for all actions and versions  
✅ Track governance and data quality KPIs  
✅ Visualize results in Streamlit (Power BI optional)

---

## 🧰 Tech Stack

- **Python**: `pandas`, `Streamlit`, `matplotlib`
- **Jupyter Notebooks**: data preparation, KPI analysis
- **Power BI Desktop** *(optional)*: for BI dashboarding
- **Excel (.xlsx)**: raw data format
- **BPMN** *(optional)*: process modeling

---

## 📁 Project Structure

```bash
material-master-data-simulation/
├── data/
│   ├── Online Retail.xlsx              # Raw dataset
│   ├── cleaned_retail_data.csv         # Cleaned dataset
│   ├── simulated_material_master.csv   # Simulated material master data
│   ├── material_workflow.csv           # Workflow state store
│   └── material_master_audit.csv       # Audit log of approvals/changes
│
├── dashboards/
│   ├── streamlit_app.py                # Material data dashboard
│   ├── workflow_app.py                 # Workflow simulation app
│   └── powerbi_dashboard.pbix          # Power BI dashboard (optional)
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb          # Prepare master data
│   └── 02_kpi_analysis.ipynb           # Prototype KPIs
│
├── docs/
│   └── data_governance_policy.md       # Roles, rules, and responsibilities
│
├── src/
│   ├── __init__.py
│   ├── data_cleaner.py
│   ├── data_loader.py
│   ├── governance.py
│   └── kpi_calculator.py
│
├── validate_material_master.py         # Standalone validator script
├── requirements.txt
└── README.md
````

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/material-master-data-simulation.git
cd material-master-data-simulation
```

### 2. Create a virtual environment and install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add dataset

Place `Online Retail.xlsx` inside the `data/` folder.

### 4. Run Streamlit apps

```bash
# For KPI dashboard (materials overview)
streamlit run dashboards/streamlit_app.py

# For workflow simulation (request → approve)
streamlit run dashboards/workflow_app.py
```

---

## 📊 KPIs Tracked

### 🔍 Data Quality KPIs

* 🧼 Material data completeness
* 🔁 Duplicate material detection
* ⚠️ Top errors by field
* 📉 Data quality score *(planned)*
* ❗ Short or missing descriptions

### ⏱ Workflow KPIs

* 📦 Total material requests
* ✅ Number of approved materials
* 📈 Approval rate (%)
* ⏳ Average approval time (days)

These are live in both Streamlit apps and Power BI (optional).

---

## 🏛️ Data Governance Policy

Includes roles, validations, versioning rules, and approval flow documentation.

📄 See [`docs/data_governance_policy.md`](docs/data_governance_policy.md)

---

## 📌 Roadmap Ideas

* [ ] Add user roles and login simulation
* [ ] SLA breach warnings (e.g. overdue requests)
* [ ] Trigger email-like notifications
* [ ] Extend to Customer/Vendor master domains
* [ ] Enable multi-level approval (tiered workflow)

---

## ✅ Ideal For

* Practicing **SAP-style Master Data Governance**
* Showcasing **data quality & workflow automation**
* Building a portfolio project for **data architect** or **analyst** roles
* Demonstrating real-world **KPI tracking** and **dashboarding**

---
