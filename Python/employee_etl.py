import pandas as pd
import os
from datetime import datetime

# ============================================================
# EMPLOYEE ETL PROJECT
# ============================================================

print("=" * 60)
print("          EMPLOYEE ETL STARTED")
print("=" * 60)

start_time = datetime.now()
print("Execution Started :", start_time)

# ============================================================
# PROJECT PATHS
# ============================================================

base_folder = r"C:\SSIS\Employee_ETL_Project"

input_folder = os.path.join(base_folder, "Input")
output_folder = os.path.join(base_folder, "Output")

input_file = os.path.join(input_folder, "Employee.csv")

os.makedirs(output_folder, exist_ok=True)

# ============================================================
# READ CSV
# ============================================================

df = pd.read_csv(input_file)

print("\nOriginal Employee Data")
print(df)

# ============================================================
# REMOVE DUPLICATES
# ============================================================

print("\nRemoving Duplicate Employee IDs...")

duplicate_count = df.duplicated(subset=["EmployeeID"]).sum()

print("Duplicate Records Found :", duplicate_count)

df = df.drop_duplicates(subset=["EmployeeID"])

print("Duplicate Records Removed Successfully.")

# ============================================================
# HANDLE NULL VALUES
# ============================================================

print("\nHandling Missing Values...")

df["EmployeeName"] = df["EmployeeName"].fillna("Not Available")
df["Department"] = df["Department"].fillna("Unknown")

print("Missing Values Handled Successfully.")

# ============================================================
# REMOVE LEADING AND TRAILING SPACES
# ============================================================

df["EmployeeName"] = df["EmployeeName"].astype(str).str.strip()
df["Email"] = df["Email"].astype(str).str.strip()
df["Department"] = df["Department"].astype(str).str.strip()

print("\nLeading and Trailing Spaces Removed Successfully.")

# ============================================================
# CREATE ERROR DATAFRAMES
# ============================================================

# Invalid Email
invalid_email = df[
    ~df["Email"].str.contains("@", na=False)
].copy()

invalid_email["ErrorReason"] = "Invalid Email"

# Negative Salary
invalid_salary = df[
    df["Salary"] <= 0
].copy()

invalid_salary["ErrorReason"] = "Negative Salary"

# Missing Employee Name
missing_name = df[
    df["EmployeeName"] == "Not Available"
].copy()

missing_name["ErrorReason"] = "Missing Employee Name"

# Missing Department
missing_department = df[
    df["Department"] == "Unknown"
].copy()

missing_department["ErrorReason"] = "Missing Department"

# ============================================================
# COMBINE ERROR RECORDS
# ============================================================

error_records = pd.concat(
    [
        invalid_email,
        invalid_salary,
        missing_name,
        missing_department
    ],
    ignore_index=True
)

# Remove duplicate error rows
error_records = error_records.drop_duplicates(subset=["EmployeeID"])

print("\nError Records")
print(error_records)

# ============================================================
# REMOVE ERROR RECORDS FROM CLEAN DATA
# ============================================================

clean_data = df[
    ~df["EmployeeID"].isin(error_records["EmployeeID"])
].copy()

print("\nClean Employee Data")
print(clean_data)

# ============================================================
# COUNTS
# ============================================================

total_rows = len(df)
loaded_rows = len(clean_data)
rejected_rows = len(error_records)

# ============================================================
# SAVE CLEAN FILE
# ============================================================

clean_file = os.path.join(output_folder, "Employee_Clean.csv")

if os.path.exists(clean_file):
    os.remove(clean_file)

clean_data.to_csv(clean_file, index=False)

print("\nEmployee_Clean.csv Saved Successfully")

# ============================================================
# SAVE ERROR FILE
# ============================================================

error_file = os.path.join(output_folder, "Employee_Error.csv")

if os.path.exists(error_file):
    os.remove(error_file)

error_records.to_csv(error_file, index=False)

print("Employee_Error.csv Saved Successfully")

# ============================================================
# SAVE ETL COUNT FILE
# ============================================================

count_file = os.path.join(output_folder, "ETL_Count.csv")

if os.path.exists(count_file):
    os.remove(count_file)

end_time = datetime.now()

etl_count = pd.DataFrame({
    "PackageName": ["Employee_ETL_Project"],
    "TotalRows": [total_rows],
    "LoadedRows": [loaded_rows],
    "RejectedRows": [rejected_rows],
    "StartTime": [start_time.strftime("%Y-%m-%d %H:%M:%S")],
    "EndTime": [end_time.strftime("%Y-%m-%d %H:%M:%S")],
    "PackageStatus": ["Success"]
})

etl_count.to_csv(count_file, index=False)

print("ETL_Count.csv Saved Successfully")

# ============================================================
# ETL SUMMARY
# ============================================================

print("\n========== ETL SUMMARY ==========")

print("Package Name      : Employee_ETL_Project")
print("Total Input Rows  :", total_rows)
print("Loaded Rows       :", loaded_rows)
print("Rejected Rows     :", rejected_rows)
print("Duplicate Rows    :", duplicate_count)

print("\nOutput Files")
print("Clean File :", clean_file)
print("Error File :", error_file)
print("Count File :", count_file)

# ============================================================
# ETL END
# ============================================================

print("\nExecution Completed :", end_time)
print("Execution Time :", end_time - start_time)

print("=" * 60)
print("     EMPLOYEE ETL COMPLETED SUCCESSFULLY")
print("=" * 60)