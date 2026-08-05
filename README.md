# Employee ETL Pipeline using SSIS, Python & SQL Server

📌 Project Overview
This project demonstrates a complete End-to-End ETL (Extract, Transform, Load) pipeline using SQL Server Integration Services (SSIS), Python, and SQL Server.

The pipeline reads employee data from a CSV file, validates and cleans the data using Python, loads valid records into SQL Server, stores invalid records in an error file, and records ETL execution statistics in an audit log table.

---

🛠️ Technologies Used

- SQL Server
- SQL Server Integration Services (SSIS)
- Python
- SQL
- Visual Studio 2022
- Git & GitHub

---

📂 Project Structure

```
Employee-ETL-Pipeline-SSIS-Python-SQLServer
│
├── Input/
│   └── Employee.csv
│
├── Output/
│   ├── Employee_Clean.csv
│   ├── Employee_Error.csv
│   └── ETL_Count.csv
│
├── Python/
│   └── employee_etl.py
│
├── SQL/
│   └── SQLQuery1.sql
│
├── Employee_ETL_Project/
│   └── SSIS Package
│
└── README.md


🔄 ETL Workflow

Step 1 - Extract
- Read employee data from Employee.csv.

Step 2 - Transform
Python validates the data by:
- Checking missing values
- Validating email format
- Removing duplicate Employee IDs
- Validating salary values
- Cleaning invalid records

Step 3 - Load
SSIS loads:
- Valid records into SQL Server
- Invalid records into Employee_Error.csv
- Audit details into ETL_Log table

---

📊 Database Tables

Employee_Master

- EmployeeID
- EmployeeName
- Email
- Department
- Salary
- JoiningDate

ETL_Log

- AuditID
- PackageName
- TotalRows
- LoadedRows
- RejectedRows
- StartTime
- EndTime
- Status

---

📁 Output Files

Employee_Clean.csv
Contains valid employee records.

Employee_Error.csv
Contains rejected records with validation errors.

ETL_Count.csv
Contains ETL execution summary.

---

▶️ How to Run

1. Open the SSIS project in Visual Studio.
2. Execute SQLQuery1.sql to create the database and tables.
3. Place Employee.csv inside the Input folder.
4. Run the SSIS package.
5. Verify data in SQL Server and Output folder.

---

📷 Screenshots

Add screenshots here:

- SSIS Control Flow
- SQL Tables
- Input CSV
- Output Files
- SQL Server Results

---

🚀 Features

- End-to-End ETL Pipeline
- Python Data Validation
- SSIS Data Flow
- Error Handling
- Audit Logging
- SQL Server Integration
- GitHub Version Control

---

📈 Future Improvements

- Incremental Loading
- Email Notifications
- Azure Data Factory Integration
- Power BI Dashboard
- Azure SQL Database Deployment

---

👨‍💻 Author

**Shubham Shinde**

GitHub:
https://github.com/Shubh2511-git
