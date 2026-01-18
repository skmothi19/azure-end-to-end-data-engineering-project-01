\# End-to-End Azure Data Engineering Pipeline



\## 📖 Project Overview

This project demonstrates an end-to-end batch data engineering pipeline built on Microsoft Azure.

The pipeline ingests raw CSV data, processes it using a layered architecture, and prepares

analytics-ready datasets.



---



\## 🏗️ Architecture

Source CSV  

→ Azure Data Factory  

→ ADLS Gen2 (Bronze)  

→ Azure Databricks (PySpark)  

→ ADLS Gen2 (Silver \& Gold)  

→ Analytics / BI



---



\## 🧰 Technologies Used

\- Azure Data Factory (ADF)

\- Azure Data Lake Storage Gen2

\- Azure Databricks

\- PySpark

\- Parquet



---



\## 🔄 Data Flow



\### Bronze Layer

\- Raw CSV ingested using Azure Data Factory

\- No schema enforcement

\- Append-only for traceability



\### Silver Layer

\- Data cleaned and standardized using PySpark

\- Column names normalized

\- Stored as Parquet



\### Gold Layer

\- Business-ready aggregated data

\- Example: Customer count by country

\- Optimized for analytics



---



\## 🔐 Security Note

During development, storage account keys were temporarily used to unblock progress.

In production, Managed Identity with RBAC is recommended.



---



\## 🎯 Skills Demonstrated

\- End-to-end Azure data pipelines

\- Batch processing with PySpark

\- Layered data lake architecture

\- Data quality handling



