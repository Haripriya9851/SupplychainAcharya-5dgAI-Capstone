from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig
from tools import list_tables_tool, describe_table_tool
from Utils.config import GOOGLE_API_KEY


class SQLGeneratorAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            google_api_key=GOOGLE_API_KEY,
            temperature=0.2
        )
        self.tools = [list_tables_tool, describe_table_tool]

        self.instruction = """
        You are a SQL code generator for a supply chain database.

        You MUST use the following tools to understand the schema before writing queries:
        - listlist_tables_tool_tables
        - describe_table(table_name)

        DO NOT assume the schema.
        DO NOT invent column names.

        You are generating a SQL query to run on a real SQLite database using these tools.

        Respond only with the SQL query, nothing else.
        """

        self.config = RunnableConfig(
            config={
                "configurable": {"tools": self.tools},
                "system_instruction": self.instruction
            }
        )

    def run(self, state: dict) -> dict:
        print("🛠️ SQLGeneratorAgent: Generating SQL with Gemini...")
        user_query = state.get("user_query", "").strip()

        prompt = f"""
        The user asked: \"{user_query}\" , for example, Why eggs out of stock at store 1?

        Think step-by-step:
        1. Use the tools provided to explore the database schema with list_tables() and ge
        2. Then generate a valid SELECT SQL query to fulfill the user's intent.
        3. Do NOT guess column names or table names — use the tools.

        Return ONLY the SQL query.

        
        """
        response = self.llm.invoke([HumanMessage(content=prompt)], config=self.config)
        sql = response.content.strip()
        print(sql)
        state["generated_sql"] = sql
        return state
