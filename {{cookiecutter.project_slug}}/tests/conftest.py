import pytest
from pyspark.sql import SparkSession

@pytest.fixture(scope="session")
def spark():
    session = SparkSession.builder.master("local[*]").appName("test-session").getOrCreate()
    yield session
    session.stop()
