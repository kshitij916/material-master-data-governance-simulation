import streamlit as st
import pandas as pd
import os

# --- File Paths ---
WORKFLOW_PATH = "data/material_workflow.csv"
AUDIT_PATH = "data/material_master_audit.csv"

# --- Load Workflow Data ---
if os.path.exists(WORKFLOW_PATH):
    workflow_df = pd.read_csv(WORKFLOW_PATH)
else:
    workflow_df = pd.DataFrame(columns=[
        "MaterialNumber", "MaterialDescription", "RequestDate", "RequestedBy",
        "Status", "ApprovedBy", "ApprovalDate", "Comments"
    ])

# --- Load Audit Log Data ---
if os.path.exists(AUDIT_PATH):
    audit_df = pd.read_csv(AUDIT_PATH)
else:
    audit_df = pd.DataFrame(columns=[
        "MaterialNumber", "MaterialDescription", "Status",
        "CreatedBy", "CreatedAt", "ModifiedBy", "ModifiedAt",
        "Version", "Comments"
    ])

# --- Streamlit Config ---
st.set_page_config(page_title="Material Master Workflow", layout="wide")
st.title("🛠️ Material Master Data Workflow")

# --- Section 1: Submit Request ---
with st.form("material_request_form"):
    st.subheader("📥 Submit New Material Request")
    mat_num = st.text_input("Material Number")
    mat_desc = st.text_input("Material Description")
    requested_by = st.text_input("Requested By")
    submitted = st.form_submit_button("Submit Request")

    if submitted:
        if not mat_num or not mat_desc or not requested_by:
            st.error("⚠️ Please fill all fields.")
        else:
            new_entry = {
                "MaterialNumber": mat_num,
                "MaterialDescription": mat_desc,
                "RequestDate": pd.Timestamp.now(),
                "RequestedBy": requested_by,
                "Status": "Requested",
                "ApprovedBy": "",
                "ApprovalDate": "",
                "Comments": ""
            }
            workflow_df = pd.concat([workflow_df, pd.DataFrame([new_entry])], ignore_index=True)
            workflow_df.to_csv(WORKFLOW_PATH, index=False)
            st.success(f"✅ Request for material `{mat_num}` submitted!")

# --- Section 2: Approvals ---
st.markdown("---")
st.subheader("✅ Approve Pending Material Requests")

pending_df = workflow_df[workflow_df["Status"] == "Requested"]

if pending_df.empty:
    st.info("No pending approvals.")
else:
    for idx, row in pending_df.iterrows():
        with st.expander(f"🔍 {row['MaterialNumber']} — {row['MaterialDescription']}"):
            approver = st.text_input("Approver Name", key=f"approver_{idx}")
            comments = st.text_area("Comments", key=f"comment_{idx}")
            if st.button("Approve", key=f"approve_{idx}"):
                # Update workflow record
                workflow_df.loc[idx, "Status"] = "Approved"
                workflow_df.loc[idx, "ApprovedBy"] = approver
                workflow_df.loc[idx, "ApprovalDate"] = pd.Timestamp.now()
                workflow_df.loc[idx, "Comments"] = comments
                workflow_df.to_csv(WORKFLOW_PATH, index=False)

                # Create audit log entry
                new_log = {
                    "MaterialNumber": row["MaterialNumber"],
                    "MaterialDescription": row["MaterialDescription"],
                    "Status": "Approved",
                    "CreatedBy": row["RequestedBy"],
                    "CreatedAt": row["RequestDate"],
                    "ModifiedBy": approver,
                    "ModifiedAt": pd.Timestamp.now(),
                    "Version": 1,  # Future updates can increment this
                    "Comments": comments
                }

                audit_df = pd.concat([audit_df, pd.DataFrame([new_log])], ignore_index=True)
                audit_df.to_csv(AUDIT_PATH, index=False)

                st.success(f"✅ Material {row['MaterialNumber']} approved.")
                st.rerun()

# --- Section 3: All Workflow Requests Table ---
st.markdown("---")
st.subheader("📋 All Workflow Records")

# Convert datetime columns to strings before displaying
workflow_display_df = workflow_df.copy()
if "RequestDate" in workflow_display_df.columns:
    workflow_display_df["RequestDate"] = workflow_display_df["RequestDate"].astype(str)
if "ApprovalDate" in workflow_display_df.columns:
    workflow_display_df["ApprovalDate"] = workflow_display_df["ApprovalDate"].astype(str)

st.dataframe(workflow_display_df)

# --- Section 4: Audit Log Viewer ---
st.markdown("---")
st.subheader("📑 Material Audit Log Viewer")

if audit_df.empty:
    st.info("No audit records yet.")
else:
    material_list = audit_df["MaterialNumber"].unique().tolist()
    selected_mat = st.selectbox("🔎 Select Material Number", material_list)

    if selected_mat:
        mat_history = audit_df[audit_df["MaterialNumber"] == selected_mat]
        mat_history = mat_history.sort_values("Version")

        # Convert datetime columns to strings before displaying
        mat_history_display = mat_history.copy()
        if "CreatedAt" in mat_history_display.columns:
            mat_history_display["CreatedAt"] = mat_history_display["CreatedAt"].astype(str)
        if "ModifiedAt" in mat_history_display.columns:
            mat_history_display["ModifiedAt"] = mat_history_display["ModifiedAt"].astype(str)

        st.write(f"Showing version history for **{selected_mat}**:")
        st.dataframe(mat_history_display)

# --- Section 5: Data Quality & Workflow KPIs ---
st.markdown("---")
st.subheader("📊 Data Quality & Workflow KPIs")

# Calculate KPIs
total_requests = len(workflow_df)
total_approved = len(workflow_df[workflow_df["Status"] == "Approved"])
approval_rate = (total_approved / total_requests * 100) if total_requests > 0 else 0

# Approval time
workflow_df["RequestDate"] = pd.to_datetime(workflow_df["RequestDate"], errors='coerce')
workflow_df["ApprovalDate"] = pd.to_datetime(workflow_df["ApprovalDate"], errors='coerce')
approved_df = workflow_df.dropna(subset=["ApprovalDate"])
approval_times = (approved_df["ApprovalDate"] - approved_df["RequestDate"]).dt.days
avg_approval_days = round(approval_times.mean(), 2) if not approval_times.empty else 0

# Duplicate materials
dup_count = workflow_df["MaterialNumber"].duplicated().sum()

# Short or missing descriptions
invalid_descriptions = workflow_df["MaterialDescription"].apply(lambda x: pd.isna(x) or len(str(x)) < 5).sum()

# Show KPIs
col1, col2, col3 = st.columns(3)
col1.metric("📦 Total Requests", total_requests)
col2.metric("✅ Approved", total_approved)
col3.metric("📈 Approval Rate", f"{approval_rate:.1f} %")

col4, col5, col6 = st.columns(3)
col4.metric("⏱️ Avg Approval Time (days)", avg_approval_days)
col5.metric("🛑 Duplicate Material Numbers", dup_count)
col6.metric("🧼 Short/Missing Descriptions", invalid_descriptions)
