import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.sql.functions import col, round, to_date, year, month, dayofmonth, date_format
from awsglue.job import Job

# Accept dynamic arguments for job name, input and output paths
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'input_path', 'output_path'])

input_path = args['input_path']
output_path = args['output_path']

# Initialize contexts
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read CSV from S3
df = spark.read.option("header", True).option("inferSchema", True).csv(input_path)

# Filter out cancelled transactions (InvoiceNo starting with "C")
df_clean = df.filter(~col("InvoiceNo").startswith("C"))

# Filter only numeric InvoiceNos
df_clean = df_clean.filter(col("InvoiceNo").rlike("^[0-9]+$"))

# Cast InvoiceNo to Integer
df_clean = df_clean.withColumn("InvoiceNo", col("InvoiceNo").cast("int"))

# Remove nulls and negative values
df_clean = df_clean.filter(
    (col("Quantity") >= 0) &
    (col("UnitPrice") > 0) &
    (col("Description").isNotNull()) &
    (col("CustomerID").isNotNull())
)

# Add TotalPrice column
df_clean = df_clean.withColumn("TotalPrice", round(col("Quantity") * col("UnitPrice"), 2))

# Format InvoiceDate and extract parts
df_clean = df_clean.withColumn("InvoiceDate", to_date(col("InvoiceDate"), "dd-MM-yyyy HH:mm"))
df_clean = df_clean.withColumn("Year", year(col("InvoiceDate")))
df_clean = df_clean.withColumn("Month", month(col("InvoiceDate")))
df_clean = df_clean.withColumn("Day", dayofmonth(col("InvoiceDate")))
df_clean = df_clean.withColumn("Weekday", date_format(col("InvoiceDate"), "EEEE"))

# Write cleaned data as single parquet file
df_clean.coalesce(1).write.mode("overwrite").parquet(output_path)

print("✅ Data cleaning and export to Parquet completed successfully.")

job.commit()
