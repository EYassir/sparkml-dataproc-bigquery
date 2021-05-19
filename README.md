# Dataproc, BigQuery and Apache Spark ML
Example machine learning performed with sparkML and bigquery connector

# Objectives
Use linear regression to build a model of birth weight as a function of five factors:
* gestation weeks
* mother’s age
* father’s age
* mother’s weight gain during pregnancy
* Apgar score

BigQuery is used to prepare the linear regression input table, which is written to your Google Cloud Platform project. Python is used to query and manage data in BigQuery. The resulting linear regression table is accessed in Apache Spark, and Spark ML is used to build and evaluate the model. A Dataproc PySpark job is used to invoke Spark ML functions.

# Usage
```bash
git clone https://github.com/EYassir/sparkml-dataproc-bigquery.git

chmod +x run_pipeline

./run_pipeline
```