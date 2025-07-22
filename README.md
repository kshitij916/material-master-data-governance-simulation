# 📦 Material Master Data Governance Simulation

This project simulates an end-to-end **Material Master Data Management System** using the [Online Retail dataset (UCI ML Repo)](https://archive.ics.uci.edu/ml/datasets/online+retail). It models how enterprises manage material creation workflows, approvals, audit trails, governance policies, and KPIs — similar to **SAP ERP master data processes**.

---

## 🧩 Core Features

✅ Clean and standardize raw transactional data
✅ Generate enriched Material Master records from retail transactions
✅ Request → Approve → Create material lifecycle with form-based input
✅ Maintain full audit trail and version history
✅ Track data quality and governance KPIs
✅ Visualize data in **Streamlit** (real-time) and **Power BI** (optional)
✅ Simulate real enterprise workflows with data stewardship and compliance

---

## 🧰 Tech Stack

| Purpose                 | Tools / Libraries                       |
| ----------------------- | --------------------------------------- |
| 📊 Data Processing      | `pandas`, `numpy`, `openpyxl`           |
| 🧹 Preprocessing        | Jupyter Notebooks                       |
| 🖥️ Workflow Simulation | `streamlit`, file-based persistence     |
| 🧾 Audit Trail          | CSV versioning with timestamps/comments |
| 📈 Dashboards           | `Streamlit`, `Power BI Desktop`         |
| 🛡️ Governance Modeling | Markdown + Rules-based enforcement      |

---

## 📁 Project Structure

```bash
material-master-data-simulation/
├── data/
│   ├── Online Retail.xlsx              # Raw dataset (UCI ML)
│   ├── cleaned_retail_data.csv         # Cleaned + enriched
│   ├── simulated_material_master.csv   # Master data records
│   ├── material_workflow.csv           # Workflow state store
│   └── material_master_audit.csv       # Full version history
│
├── dashboards/
│   ├── streamlit_app.py                # KPI dashboard
│   ├── workflow_app.py                 # Workflow + audit manager
│   └── powerbi_dashboard.pbix          # Optional Power BI dashboard
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb          # Clean raw Excel data
│   └── 02_kpi_analysis.ipynb           # Prototype KPIs
│
├── docs/
│   └── data_governance_policy.md       # Governance rules + roles
│
├── src/
│   ├── __init__.py
│   ├── data_cleaner.py                 # Reusable cleaner logic
│   ├── data_loader.py                  # Load/transform logic
│   ├── governance.py                   # Governance validation rules
│   └── kpi_calculator.py               # Reusable KPI generators
│
├── validate_material_master.py         # Quick validator CLI
├── requirements.txt
└── README.md
```

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

### 3. Add Dataset

Download [`Online Retail.xlsx`](https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx) and place it inside the `data/` folder.

### 4. Run the Apps

```bash
# Launch KPI dashboard
streamlit run dashboards/streamlit_app.py

# Launch workflow simulation (request, approve, audit)
streamlit run dashboards/workflow_app.py
```

---

## 📊 KPIs Tracked

### 🧹 Data Quality KPIs

* 🧼 Completeness by field
* 🔁 Duplicate material detection
* ❗ Missing/short descriptions
* 📌 Frequency of invalid or inconsistent entries

### 🛠️ Workflow KPIs

* 📦 Total material requests
* ✅ Approved materials
* 🔁 Rejected or incomplete entries
* 📈 Approval rate (%)
* ⏱ Average approval time *(optional)*

Visualized in both Streamlit apps and **Power BI dashboard** (see `/dashboards/powerbi_dashboard.pbix`).

---

## 🏛️ Governance Policy

Documented governance logic includes:

* Role responsibilities (Requestor, Approver, Data Steward)
* Approval workflow
* Field-level validation (description, quantity, material type rules)
* Audit/versioning rules
* KPI monitoring logic

📄 See [`docs/data_governance_policy.md`](docs/data_governance_policy.md)

---

## 🎯 Real-World Relevance

This project reflects tasks of a real **Master Data & Process Architect** role:

* Central data modeling and quality enforcement
* SAP-like material master creation and governance
* Cross-functional process alignment (Logistics, Procurement, Engineering)
* End-to-end lifecycle coverage: request → approve → create → monitor
