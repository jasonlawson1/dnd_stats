import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = None

dbName = os.getenv("DB_NAME")
user = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")


def connect_to_db():
    global conn
    if conn is None:
        conn = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=dbName
        )


def close_connection():
    global conn
    if conn is not None:
        conn.close()


def get_cursor():
    global conn
    connect_to_db()
    return conn.cursor()


def get_conn():
    global conn
    connect_to_db()
    return conn
