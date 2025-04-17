from langgraph.graph import StateGraph, END
from Agents.manager_agent import ManagerAgent
from Agents.sql_generator_agent import SQLGeneratorAgent
from Agents.sql_executor_agent import SQLExecutorAgent
from Agents.root_cause_agent import RootCauseAnalyzer
from Agents.clarifier import ClarificationNode
from Graph.nodes import WelcomeNode  # or from Graph.nodes import WelcomeNode
import logging

logging.basicConfig(level=logging.INFO)

class SupplyChainGraph:
    def __init__(self):
        self.welcome = WelcomeNode()
        self.manager = ManagerAgent()
        self.sql_gen = SQLGeneratorAgent()
        self.sql_exec = SQLExecutorAgent()
        self.analyzer = RootCauseAnalyzer()
        self.clarifier = ClarificationNode()

    def build(self):
        builder = StateGraph(dict)
        builder.add_node("welcome", self.welcome.run)

        builder.add_node("human", self.clarifier.run)
        builder.add_node("manager_agent", self.manager.run)
        builder.add_node("sql_generator", self.sql_gen.run)
        builder.add_node("sql_executor", self.sql_exec.run)
        builder.add_node("root_cause", self.analyzer.run)

        builder.set_entry_point("welcome")

        def route_from_manager(state):
            """
            Determines the next node based on the state after the ManagerAgent runs.
            """
            logging.info(f"Current state: {state}")

            # Check if the user wants to quit
            if state.get("exit", False):
                logging.info("🚪 User chose to exit. Ending session.")
                return "end"

            if state.get("needs_user_input", False):
                attempts = state.get("clarification_attempts", 0) + 1
                state["clarification_attempts"] = attempts

                if attempts >= 4:
                    logging.warning("🚫 Too many clarification attempts. Ending session.")
                    state["manager_response"] = "Too many attempts. Please restart."
                    return "end"

                logging.info("Routing back to human for clarification.")
                return "human"

            logging.info("Routing to SQL generator.")
            return "sql_generator"

        builder.add_conditional_edges("manager_agent", route_from_manager, {
            "human": "human",
            "sql_generator": "sql_generator",
            "end": END
        })
        builder.add_edge("welcome", "human")               # greet → ask user input
        builder.add_edge("human", "manager_agent")         # user input → manager
        builder.add_edge("manager_agent", "sql_generator") # if validated
        builder.add_edge("sql_generator", "sql_executor")
        builder.add_edge("sql_executor", "root_cause")
        builder.add_edge("root_cause", END)


        return builder.compile()
