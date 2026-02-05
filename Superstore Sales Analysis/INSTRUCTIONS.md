# Superstore Sales Analysis & Data Visualisation

## Project Description:
This project will train you how to use PowerBI to analyze a real-world database, how to extract the most useful information from the dataset, how to pre-process the data using Python for improved performance, how to use a structured query language to retrieve useful information from the database, and how to visualize the data using the PowerBI tool.

## Download the superstore dataset:from Kaggle

Module 1: Data Pre-processing
In this Module you will be working on how to perform pre-processing of data and working on handling null values, deletion or transformation of irrelevant values, data type transformation, removing duplicates and data validations to get refined and cleaner data to perform further analysis.
When we have data first step we need to do:

## Steps to perform Data Pre-processing:
Step 1: Removing duplicate rows ( there could be duplicate rows excluding Row_ID column ).

Step 2: Removing rows for which few values are missing.

Step 3: Remove irrelevant values from each column if any. Validation of all values for a column( order date and ship date value must be in correct date format ). For each entry in dataset ship date >= order date

Step 4: Export the cleaned dataset as a .csv file: prefer UTF-8 encoding.

Step 5: Convert the pre-processed dataset into a file and import it to table named "superstore".

# Module 2: Power BI 

Step 1: Load Data
Open Power BI Desktop
Home → Get Data → CSV
Load Superstore_Raw.csv
Import cleaned_superstore.csv.

🔹 Step 2: Split Tables
@ DATA MODEL 
You should have:

Orders (Fact Table)
Customers (Dimension)
Products (Dimension)
Date table (optional but 🔥)

Create Fact Table (Orders)
Keep only:OrderID,OrderDate,CustomerID,ProductID,Sales,Quantity,Profit
Rename table → Orders

Create Customers Table
Duplicate raw table
Keep:CustomerID,CustomerName,Segment,Region,Remove duplicates
Rename → Customers

Create Products Table
Duplicate raw table
Keep:ProductID,ProductName,Category,Sub-Category,Remove duplicates
Rename → Products

Create Date Table (DAX)
Modeling → New Table
DateTable =
ADDCOLUMNS(
    CALENDAR(MIN(Orders[OrderDate]), MAX(Orders[OrderDate])),
    "Year", YEAR([Date]),
    "Month", FORMAT([Date], "MMMM"),
    "MonthNumber", MONTH([Date]),
    "Quarter", "Q" & FORMAT([Date], "Q")
)

🔹 Step 3: Create Data Model
Go to Model View and connect:

Orders[CustomerID] → Customers[CustomerID]
Orders[ProductID] → Products[ProductID]
Orders[OrderDate] → DateTable[Date]

✅ One-to-many
✅ Single direction
✅ Star schema
I modeled the data using a star schema to optimize performance and filtering single table is fully split into a star schema.
<img src="screenshots\data_model.png" alt="Image Description" width="300">

🔹 Step 4: Create Measures (DAX)
Total Sales = SUM(Orders[Sales])
Total Profit = SUM(Orders[Profit])
Total Quantity = SUM(Orders[Quantity])
Profit Margin = DIVIDE([Total Profit], [Total Sales])

🔹 Step 5: Build Dashboard
Dashboard Pages
Page 1: Executive Overview
KPIs
Total Sales
Total Profit
Profit Margin
Quantity Sold
Sales by Region (Map/Bar)

Page 2: Trends
Monthly Sales Trend
Monthly Profit Trend

Page 3: Product Performance
Top Products by Sales
Loss-making Products

