--Database Create
CREATE DATABASE Employee_ETL_DB;


USE Employee_ETL_DB;

--Create Tables

CREATE TABLE Employee_Master
(
    EmployeeID INT PRIMARY KEY,
    EmployeeName VARCHAR(100),
    Email VARCHAR(100),
    Department VARCHAR(50),
    Salary DECIMAL(10,2),
    JoiningDate DATE
);

CREATE TABLE ETL_Log
(
    AuditID INT IDENTITY(1,1) PRIMARY KEY,
    PackageName VARCHAR(100),
    TotalRows INT,
    LoadedRows INT,
    RejectedRows INT,
    StartTime DATETIME,
    EndTime DATETIME,
    Status VARCHAR(20)
);
SELECT * FROM dbo.Employee_Master;
SELECT * FROM dbo.ETL_Log;
