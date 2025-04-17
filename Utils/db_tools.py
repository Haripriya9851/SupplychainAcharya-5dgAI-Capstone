import sqlite3
import os

DB_PATH =  "../Input/SupplyChainABC2Apr16.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def list_tables(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return [row[0] for row in cursor.fetchall()]

def describe_table(conn, table_name):
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name});")
    return [(col[1], col[2]) for col in cursor.fetchall()]

def execute_query(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    return cursor.fetchall()
