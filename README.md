# Finance Accounts Payable Data Pipeline

## Project Overview

This project demonstrates an end-to-end ETL pipeline for Finance Accounts Payable data.

## Tech Stack

- Python
- Pandas
- SQL
- SQLite
- Apache Airflow
- Git
- GitHub
- Power BI

## Workflow

Raw Invoice CSV
↓

Extract using Python

↓

Transform
- Remove duplicate invoices
- Validate data

↓

Load

↓

SQLite Database

↓

SQL Reporting

↓

Power BI Dashboard

## Features

- ETL Pipeline
- Duplicate Detection
- SQL Reporting
- Vendor Analysis
- Payment Status Report
- Invoice Analytics

## Folder Structure

scripts/

data/

sql/

airflow_dags/

powerbi/

## Future Improvements

- Snowflake Integration
- AWS S3
- Apache Spark
- CI/CD Pipeline