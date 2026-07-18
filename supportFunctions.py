from pyspark.sql import SparkSession

def basicAnalysisBZTable(table: str, spark: SparkSession):
    """
    Performs and returns basic analysis on table

    Parameters
    ----------
    table : str

    Returns
    ----------
    dict:{"total count": int, schema:{str : datatype}}
    """

    df = spark.table(table)
    total_count = df.count()
    schema = df.schema.simpleString()
    return {"total_count": total_count, "schema": schema}

