from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig
from tools import execute_query_tool
from Utils.config import GOOGLE_API_KEY


class SQLExecutorAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            google_api_key=GOOGLE_API_KEY,
            temperature=0
        )
        self.tools = [execute_query_tool]

        self.instruction = """
        You are the SQL code executor using the tool execute_query_tool. 
        Your job is to execute the SQL query and return only the raw rows from the database. 
        Do not explain the results or provide any additional commentary.
        
        Always return the raw result in the same format as shown above.
        """

        self.config = RunnableConfig(
            config={
                "configurable": {"tools": self.tools},
                "system_instruction": self.instruction
            }
        )

    def run(self, state: dict) -> dict:
        print(" SQLExecutorAgent: Running SQL...")
        sql = state.get("generated_sql", "")
        prompt = f"""
        Execute the following SQL query using the tool execute_query_tool and return only the raw rows:

        SQL Query:
        ```sql
        {sql}
        ```
        Do not explain the results or provide any additional commentary.
        Always return the raw result in the same format as shown above.
        """
        response = self.llm.invoke(
            [HumanMessage(content=prompt)],
            tools=self.tools,
            config=self.config
        )
        state["executed_results"] = response.content.strip()
        return state
