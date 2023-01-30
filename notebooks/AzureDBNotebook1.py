# Databricks notebook source
from datetime import datetime
todays_date = datetime.utcnow().strftime("%m%d%Y")
filepath = "/mnt/azuredf_datasets/VehicleDetails_01252023.json"

# COMMAND ----------

df = spark.read.json(filepath)
df.show()

# COMMAND ----------

df.write.mode("append").option("mergeSchema","true").saveAsTable("DB2.VehicleDetails")