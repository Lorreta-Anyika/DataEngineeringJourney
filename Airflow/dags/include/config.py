import os
from dotenv import load_dotenv

load_dotenv("/opt/airflow/.env")

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = "host.docker.internal"
DB_PORT = "56205"
DB_NAME = "sales_db"

DATABASE_URL = (
    f"mssql+pymssql://{DB_USER}:{DB_PASS}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

DATA_SOURCE = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTIBPRSnUp10oHj5fhnUTlUJn-W7DtjSRtXIhySqW_1nZak5u4b7bPc9gTcWPHM22JL0aZJJa5QakM1/pub?gid=0&single=true&output=csv" # noqa E501