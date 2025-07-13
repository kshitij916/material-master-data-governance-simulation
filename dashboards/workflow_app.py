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
st.dataframe(workflow_df)

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
        st.write(f"Showing version history for **{selected_mat}**:")
        st.dataframe(mat_history)
