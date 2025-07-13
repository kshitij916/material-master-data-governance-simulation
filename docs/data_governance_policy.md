# 🏛️ Data Governance Policy – Material Master Data

## 📌 Purpose
This policy defines roles, responsibilities, quality rules, and processes for managing Material Master Data effectively across its lifecycle — from request to approval to creation.

---

## 🧑‍💼 Roles & Responsibilities

| Role             | Responsibility |
|------------------|----------------|
| **Data Owner**   | Accountable for material data quality, completeness, and strategic alignment |
| **Data Steward** | Ensures master data complies with business rules; performs data validation and quality checks |
| **Requester**    | Initiates material requests with required details |
| **Approver**     | Reviews and approves material records before final creation |

---

## ✅ Data Quality Rules

| Rule Category      | Description |
|--------------------|-------------|
| **Completeness**   | All required fields (Material Number, Description, Base Unit, Type) must be filled |
| **Uniqueness**     | Material Numbers must be unique |
| **Description Length** | Descriptions should be at least 5 characters |
| **Naming Convention** | Must follow pattern: `[TYPE]-[MaterialDescription]` e.g. `FERT-Screwdriver` |
| **Valid Values**   | Fields like `MaterialType`, `ProcurementType`, and `BaseUnit` must be from controlled lists |

---

## 🔁 Workflow Lifecycle

1. **Request**:
   - Any user can request a material via a form
   - Required fields must be filled

2. **Validation**:
   - Data Steward checks for:
     - Duplicates
     - Incomplete or invalid entries
     - Naming issues

3. **Approval**:
   - Approver reviews request
   - May return with comments or approve

4. **Creation**:
   - Upon approval, material is added to the Material Master
   - Record is tagged with timestamps and user metadata

---

## 🧾 Audit & Change Tracking

- All material requests and approvals are logged with:
  - `RequestedBy`, `RequestDate`
  - `ApprovedBy`, `ApprovalDate`, `Status`, and `Comments`
- Modifications to master records must create a version entry (planned in next step)

---

## 📊 Monitoring

- KPIs reported monthly via dashboard:
  - % of missing descriptions
  - Number of duplicate MaterialNumbers
  - Average approval time
  - Number of materials per type

---

## 🚫 Policy Violations

- Entries violating data quality rules will:
  - Be flagged in the dashboard
  - Be returned to requester for correction
  - Remain in “Requested” state until valid

---

## 🔐 Data Access

| User Type      | Access Level |
|----------------|--------------|
| Requester      | Submit new materials only |
| Approver       | View & approve records |
| Data Steward   | Full access with editing |
| Viewer         | Read-only |

---

## 📅 Review Cycle

This policy will be reviewed and updated **every quarter** or upon major system changes.

---

✅ **Effective Date**: 2025-07-13  
✍️ **Document Owner**: Kshitij Pandit

