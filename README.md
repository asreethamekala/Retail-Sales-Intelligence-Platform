# 🛒 Retail Sales Intelligence Platform

## 📌 Project Overview

The Retail Sales Intelligence Platform is an end-to-end data analytics project developed to analyze retail sales data and generate meaningful business insights.

The project combines Microsoft Excel, MySQL, Python, and Power BI to perform data cleaning, database management, SQL analysis, data visualization, KPI analysis, and interactive dashboard development.

The main purpose of the project is to help businesses understand sales performance, profitability, customer behavior, product performance, regional trends, and other important business metrics.

---

## 🎯 Objectives

The main objectives of this project are:

- Analyze overall sales performance.
- Analyze profitability and identify loss-making areas.
- Identify top-performing products and customers.
- Analyze sales across categories and sub-categories.
- Analyze regional sales performance.
- Analyze customer segments.
- Analyze shipping modes and order patterns.
- Calculate important business KPIs.
- Perform SQL-based business analysis.
- Create interactive Power BI dashboards.
- Create Python-based visualizations and dashboards.
- Present business insights in an easy-to-understand format.

---

## 🧰 Technologies Used

| Technology | Purpose |
|---|---|
| Microsoft Excel | Data cleaning, validation, KPI analysis and Pivot Tables |
| MySQL | Database storage and SQL analysis |
| Python | Data analysis and visualization |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Streamlit | Interactive Python dashboard |
| Power BI | Business intelligence and interactive dashboards |
| GitHub | Version control and project documentation |

---

## 📊 Dataset

The project uses a retail sales dataset containing information about:

- Orders
- Customers
- Products
- Categories
- Sub-Categories
- Sales
- Profit
- Quantity
- Discounts
- Regions
- Markets
- Shipping Modes
- Order Dates
- Ship Dates
- Customer Segments

### Dataset Size

- Total Records: 51,288
- Raw Dataset: approximately 15.1 MB
- Cleaned Dataset: approximately 12.1 MB

The dataset was cleaned and validated before being used for SQL, Python, Excel, and Power BI analysis.

---

## 🧹 Data Cleaning

The following data preparation activities were performed:

- Removed unnecessary data.
- Checked missing values.
- Checked duplicate records.
- Corrected data types.
- Standardized date fields.
- Cleaned text fields.
- Validated numerical columns.
- Checked sales and profit values.
- Created a cleaned CSV dataset.

---

## 📈 Key KPIs

| KPI | Value |
|---|---:|
| Total Sales | 22,643,618 |
| Total Profit | 1,467,442.34 |
| Total Orders | 51,288 |
| Total Customers | 3,403 |
| Total Quantity Sold | 178,303 |
| Average Sales per Record | 441.50 |
| Average Profit per Record | 28.61 |

---

## 📗 Excel Analysis

Excel was used for initial data cleaning, validation, exploratory analysis, KPI calculation, and Pivot Table analysis.

### Excel Activities

- Data cleaning
- Data validation
- KPI calculations
- Pivot Tables
- Sales analysis
- Profit analysis
- Category analysis
- Regional analysis
- Customer analysis
- Product analysis
- Shipping analysis

---

## 🗄️ SQL Analysis

MySQL was used to store and analyze the cleaned retail sales dataset.

The project includes multiple SQL analysis phases:

### Phase 1 – Database Setup

- Database creation
- Table creation
- Data types
- Primary keys

### Phase 2 – Basic SQL

- SELECT
- WHERE
- ORDER BY
- GROUP BY
- HAVING
- Aggregate functions

### Phase 3 – Advanced SQL

- Joins
- Subqueries
- Conditional analysis
- Business-oriented queries

### Phase 4 – Views

Reusable SQL views were created for analytical reporting.

### Phase 5 – Stored Procedures

Stored procedures were created for reusable business analysis.

### Phase 6 – Functions

SQL functions were implemented for reusable calculations.

### Phase 7 – Indexing and Optimization

Indexes were implemented to demonstrate query performance optimization.

### Phase 8 – Triggers

Triggers were implemented to demonstrate automated database actions.

---

## 🐍 Python Analysis

Python was used for additional analysis, database connectivity, data validation, and visualization.

### Python Libraries

- Pandas
- NumPy
- Matplotlib
- SQLAlchemy
- PyMySQL
- Streamlit

### Python Files

- `analysis.py`
- `database_connection.py`
- `import_to_mysql.py`
- `visualization.py`
- `dashboard.py`

---

## 📊 Power BI Dashboard

Power BI was used to create interactive dashboards for business intelligence and reporting.

The dashboard analyzes:

- Sales
- Profit
- Orders
- Customers
- Quantity
- Sales trends
- Profit trends
- Categories
- Products
- Regions
- Customer segments
- Shipping modes

---

## 📁 Project Structure

```text
Retail-Sales-Intelligence-Platform/
│
├── Dataset/
│   ├── Raw_Data/
│   └── Cleaned_Data/
│
├── Excel/
│   ├── Excel_Analysis.xlsx
│   └── Data_Validation.xlsx
│
├── Images/
│   ├── Dashboard_Polishing.png
│   ├── Executive_Dashboard.png
│   └── Card_Visuals.png
│
├── PowerBI/
│   └── Retail_Sales_Intelligence_Dashboard.pbix
│
├── Python/
│   ├── analysis.py
│   ├── database_connection.py
│   ├── import_to_mysql.py
│   ├── visualization.py
│   └── dashboard.py
│
├── SQL/
│   ├── Phase1_Database_Setup.sql
│   ├── Phase2_Basic_Queries.sql
│   ├── Phase3_Advanced_SQL.sql
│   ├── Phase4_Views.sql
│   ├── Phase5_Stored_Procedures.sql
│   ├── Phase6_Functions.sql
│   ├── Phase7_Indexing_Optimization.sql
│   ├── Phase8_Triggers.sql
│   └── SQL_Queries.sql
│
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore
