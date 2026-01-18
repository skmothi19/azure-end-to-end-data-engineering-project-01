# End-to-End Azure Data Engineering Pipeline

## 📖 Project Overview
This project demonstrates an end-to-end batch data engineering pipeline built on Microsoft Azure.
The pipeline ingests raw CSV data, processes it using a layered architecture, and prepares
analytics-ready datasets.

---

## 🏗️ Architecture
Source CSV → Azure Data Factory → ADLS Gen2 (Bronze)
→ Azure Databricks (PySpark)
→ ADLS Gen2 (Silver & Gold)
→ Analytics / BI

---

## 🧰 Technologies Used
- Azure Data Factory (ADF)
- Azure Data Lake Storage Gen2
- Azure Databricks
- PySpark
- Parquet
- GitHub

---

## 🔄 Data Flow Explanation

### Bronze Layer
- Raw CSV data ingested using Azure Data Factory
- No schema enforcement
- Used for traceability and reprocessing

### Silver Layer
- Data cleaned and standardized using PySpark
- Column names normalized
- Written in Parquet format for performance

### Gold Layer
- Business-ready aggregated data
- Example: Customer count by country
- Optimized for analytics and BI tools

---

## 🔐 Security Note
During development, storage account keys were temporarily used to unblock progress.
In production, Managed Identity with RBAC is recommended.

---

## 🎯 Key Learnings
- Designing layered data lake architecture
- Batch data processing with PySpark
- Azure Data Factory ingestion pipelines
- Data quality handling and transformations
