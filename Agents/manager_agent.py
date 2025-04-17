from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableConfig
from tools import list_tables_tool, describe_table_tool, execute_query_tool
from Agents.clarifier import ClarificationNode
from Utils.config import GOOGLE_API_KEY
import re
import logging

logging.basicConfig(level=logging.INFO)

class ManagerAgent:
    def __init__(self):
        self.tools = [list_tables_tool, describe_table_tool, execute_query_tool]  # Define tools first

        self.instruction ="""
        You are responsible for collecting and validating information from user in the supplychain workflow. 
        You must validate whether a user's input includes:
            - a valid store_id 
            - a valid item name 

            You MUST use tools first to understand schema of database:
            - list_tables to get the tables in db.
            - describe_table(table_name)

            DO NOT guess table names.

            Use these tools before crafting any SQL.
            Then write a SELECT query to explain with tool:
            - execute_query

            Respond with one of:
            - Validated - Stores: [id], Items: [name]
            - Missing store
            - Missing item
            - Invalid store
            - Invalid item
            - Ambiguous store
            - Ambiguous item

            DO NOT explain or greet. Just respond with the correct format.
            """
        self.config = RunnableConfig(
            config={
                "configurable": {"tools": self.tools},
                "system_instruction": self.instruction
            }
        )
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro",
            google_api_key=GOOGLE_API_KEY,
            temperature=0.2
        )
        self.clarifier = ClarificationNode()
        


    def run(self, state: dict) -> dict:
        print("🧠 ManagerAgent: Validating user input via Gemini...")
        query = state.get("user_query", "").strip()

        # Check if the query is too short or empty
        if not query or len(query.split()) < 2:
            state["manager_response"] = "🧠 Please describe your issue in more detail."
            state["needs_user_input"] = True
            return self.clarifier.run(state)

        try:
            # Invoke Gemini for validation
            response = self.llm.invoke([HumanMessage(content=query)], config=self.config)
            result = response.content.strip()
            print(f"Gemini result: {result}")

            # Validate recognized format
            keywords = ["Validated", "Missing", "Invalid", "Ambiguous"]
            if not any(result.startswith(k) for k in keywords):
                state["manager_response"] = "🤖 Please provide both store and item for analysis."
                state["needs_user_input"] = True
                return self.clarifier.run(state)

            if result.startswith("Validated"):
                # Extract store and item details
                store_ids = re.findall(r"Stores: \[(.*?)\]", result)
                item_names = re.findall(r"Items: \[(.*?)\]", result)

                state["valid_stores"] = [s.strip() for s in store_ids[0].split(",")] if store_ids and store_ids[0] else []
                state["valid_items"] = [i.strip() for i in item_names[0].split(",")] if item_names and item_names[0] else []
                print(f"✅ Parsed: stores={state['valid_stores']} | items={state['valid_items']}")

                # Handle missing details
                missing = []
                if not state["valid_stores"]:
                    missing.append("store")
                if not state["valid_items"]:
                    missing.append("item")

                if missing:
                    state["manager_response"] = f"Validated, but missing: {', '.join(missing)}. Please clarify."
                    state["needs_user_input"] = True
                    return state

                # If everything is valid
                state["manager_response"] = result
                state["needs_user_input"] = False
                return state

            elif any(result.startswith(k) for k in ["Missing", "Invalid", "Ambiguous"]):
                # Handle specific cases
                status, field = result.split()
                prompts = {
                    "Missing": f"Please provide the {field}.",
                    "Invalid": f"The {field} is not valid. Please correct it.",
                    "Ambiguous": f"The {field} is unclear. Can you specify more?",
                }
                state["manager_response"] = prompts.get(status, "Please clarify.")
                state["needs_user_input"] = True
                return state

            # Fallback for unrecognized responses
            state["manager_response"] = (
                "⚠️ I couldn't understand your request. Please provide both the store and item details, "
                "or clarify your query further."
            )
            state["needs_user_input"] = True
            return state

        except Exception as e:
            # Log the error and update the state
            logging.error(f"Error in ManagerAgent: {e}")
            state["manager_response"] = f"⚠️ Gemini failed: {e}"
            state["needs_user_input"] = True
            return state