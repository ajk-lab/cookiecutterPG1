ENV = "local"

APP_NAME = "{{ cookiecutter.spark_app_name }}"

SPARK_HOME = r"C:\path\to\spark"
HADOOP_HOME = r"C:\path\to\hadoop"

MASTER_PORT = 7077
MASTER_WEBUI_PORT = 8080
WORKER_WEBUI_PORT = 8081

WAREHOUSE_DIR = r"./spark-warehouse"
LOCAL_DIR = r"./spark-local"
LOG_DIR = r"./logs"
