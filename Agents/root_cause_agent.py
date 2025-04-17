from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from Utils.config import GOOGLE_API_KEY

class RootCauseAnalyzer:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro",
            google_api_key=GOOGLE_API_KEY,
            temperature=0.3
        )
        
    def run(self, state: dict) -> dict:
        print("🔍 RootCauseAgent: Analyzing result...")
        
        prompt = f"""
            You are a supply chain assistant.

            The user asked:
            \"\"\"{state.get("user_query")}\"\"\"

            The following is the result of an SQL query related to this request:
            {state.get("executed_results")}

            Please:
            1. Explain the most relevant insight from the result.
            2. Recommend next steps or actions.
            3. If helpful, suggest a follow-up question the user could ask.

            Only return a helpful, concise response — no explanation of what SQL is or how it works.
            Do not include any SQL code or technical jargon.
            Response:
            
            
            """
        
        response = self.llm.invoke([HumanMessage(content=prompt)])
        state["root_cause_summary"] = response.content.strip()
        return state
