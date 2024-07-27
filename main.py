from awsglue.context import GlueContext
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.dynamicframe import DynamicFrame
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, unix_timestamp, when, lit
from pyspark.sql.types import TimestampType
import sys

def transform_data(database: str, table_source: str, table_target: str) -> None:
    sc = SparkContext()
    glueContext = GlueContext(sc)
    spark = glueContext.spark_session

    dyf = glueContext.create_dynamic_frame.from_catalog(database=database, table_name=table_source)
    df = dyf.toDF()

    df = (df.withColumn("open_dt", col("open_dt").cast(TimestampType()))
            .withColumn("closed_dt", col("closed_dt").cast(TimestampType()))
            .withColumn("target_dt", col("target_dt").cast(TimestampType())))

    df = df.withColumn("delay_days", when(
        col("closed_dt") > col("target_dt"),
        (unix_timestamp(col("closed_dt")) - unix_timestamp(col("target_dt"))) / 86400
    ).otherwise(0))

    columns_to_keep = [
        "case_enquiry_id",
        "open_dt",
        "closed_dt",
        "target_dt",
        "case_status",
        "ontime",
        "closure_reason",
        "case_title",
        "subject",
        "reason",
        "neighborhood",
        "location_street_name",
        "location_zipcode",
        "latitude",
        "longitude",
        "source",
        "delay_days",
    ]

    df_selected = df.select(columns_to_keep)
    df_selected.createOrReplaceTempView("Boston_311_data")

    query = """
    SELECT * FROM Boston_311_data
    WHERE case_status = 'Closed' AND delay_days > 0
    ORDER BY delay_days DESC
    """

    result_df = spark.sql(query)
    result_df.write.mode("overwrite").format("parquet").save("s3://glue-etl-job1/gold/processed_data/")
    spark.stop()

if __name__ == "__main__":
    database = "datalake-aws"  # Nome do banco de dados no Glue Data Catalog
    table_source = "bronzebronze"      # Nome da tabela de origem no Glue Data Catalog
    table_target = "gold"        # Nome da tabela de destino no Glue Data Catalog ou caminho S3

    transform_data(database, table_source, table_target)
