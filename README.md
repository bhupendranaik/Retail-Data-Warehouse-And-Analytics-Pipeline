# 🛒 Retail-Data-Warehouse-And-Analytics-Dashboard
A cloud-based retail data solution that automates the end to end flow of data from ingestion and transformation using AWS services (S3, Lambda, Glue) to warehousing in Amazon Redshift and interactive reporting with Power BI.

## 📌 Overview

This project demonstrates a cloud-based **retail data pipeline** using *AWS Services*. It automates the **ingestion**, **transformation**, **storage**, and **visualization** of retail sales data for reporting and analytics.

---

## 🧱 Architecture

1. **Input S3 Bucket**  
   Raw retail CSV files are uploaded here.

2. **AWS Lambda**  
   Triggers a Glue job whenever a new file is uploaded to the input S3 bucket.

3. **AWS Glue Job**  
   Transforms raw CSV into structured *Parquet* format.

4. **Output S3 Bucket**  
   Stores the processed Parquet files.

5. **Amazon Redshift**  
   Loads structured data from the output S3 bucket for analysis using the COPY command or Glue Redshift connector.

6. **Power BI**  
   Connects to Redshift (via Redshift ODBC or Athena ODBC) to visualize and explore retail metrics.

---

## 🔧 Tools & Services Used

- **AWS S3** – Storage for raw and processed data  
- **AWS Lambda** – Serverless trigger for Glue jobs  
- **AWS Glue** – Serverless ETL service  
- **Amazon Redshift** – Scalable cloud data warehouse  
- **Power BI** – Interactive dashboards and reporting

---

## 🎯 Key Features

- Fully serverless ETL pipeline  
- Auto-triggered processing on new data  
- Scalable and cost-optimized architecture  
- Real-time insights via BI integration

---

## 🚀 Future Improvements

- Implement data partitioning in Glue for better query performance  
- Add detailed error handling and logging in Lambda  
- Automate Redshift data loading using Glue workflows or Lambda  
- Use **Amazon EventBridge** for scheduled ETL runs and orchestration
