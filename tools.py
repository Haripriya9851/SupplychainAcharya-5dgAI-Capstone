from langchain.tools import tool
from Utils.db_tools import get_connection, list_tables, describe_table, execute_query

@tool
def list_tables_tool() -> list:
    """List all table names in the database."""
    conn = get_connection()
    return list_tables(conn)

@tool
def describe_table_tool(table_name: str) -> list:
    """Describe the schema of a given table."""
    conn = get_connection()
    return describe_table(conn, table_name)

@tool
def execute_query_tool(sql: str) -> list:
    """Execute a SQL SELECT query and return the results."""
    conn = get_connection()
    return execute_query(conn, sql)

