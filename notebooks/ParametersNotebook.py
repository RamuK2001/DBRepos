# Databricks notebook source
dbutils.widgets.text("writeMode","overwrite")

# COMMAND ----------

writeMode = dbutils.widgets.get("writeMode")

# COMMAND ----------

if(writeMode == "append"):
    result = dbutils.notebook.run("AppendNotebook",60)
elif(writeMode == "overwrite"):
    result = dbutils.notebook.run("OverwriteNotebook",60)
else:
    dbutils.notebook.exit("Wrong input parameter")

# COMMAND ----------

print(result)