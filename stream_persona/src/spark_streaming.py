import logging
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField,FloatType,IntegerType,StringType
from pyspark.sql.functions import from_json,col

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')
logger = logging.getLogger("spark_structured_streaming")


def create_spark_session():
    """
    Creates the Spark Session with suitable configs.
    """
    try:
        # Spark session is established with cassandra and kafka jars. Suitable versions can be found in Maven repository.
        spark = SparkSession \
                .builder \
                .appName("SparkStructuredStreaming") \
                .config("spark.jars.packages", "com.datastax.spark:spark-cassandra-connector_2.12:3.0.0,org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.0") \
                .config("spark.cassandra.connection.host", "cassandra") \
                .config("spark.cassandra.connection.port","9042")\
                .config("spark.cassandra.auth.username", "cassandra") \
                .config("spark.cassandra.auth.password", "cassandra") \
                .getOrCreate()
        spark.sparkContext.setLogLevel("ERROR")
        logging.info('Spark session created successfully')
    except Exception:
        logging.error("Couldn't create the spark session")

    return spark